from enum import IntEnum
from functools import total_ordering
from typing import Any, Callable, Final, Iterable

suits: Final[tuple[str]] = ("C", "D", "H", "S")

def parse_card_value(card_value_key: str) -> int:
    """Returns numerical value of given card value key, e.g. "K" -> 13."""
    if len(card_value_key) != 1:
            raise ValueError(f"invalid card value key length: {card_value_key}")
    if card_value_key.isdigit():
        card_value = int(card_value_key)
        if card_value < 2 or card_value > 9:
            raise ValueError(f"invalid card value number: {card_value_key}")
        return card_value
    if card_value_key == "T":
        return 10
    if card_value_key == "J":
        return 11
    if card_value_key == "Q":
        return 12
    if card_value_key == "K":
        return 13
    if card_value_key == "A":
        return 14
    raise ValueError(f"invalid card value key: {card_value_key}")

@total_ordering
class Card:
    """Represents a card of a given numerical value and suit."""
    def __init__(self, card_key: str) -> None:
        """Create a card from the given card key, e.g. "2H", "TC", "AS", etc."""
        if len(card_key) != 2:
            raise ValueError(f"invalid card key length: {card_key}")
        card_value_key = card_key[0]
        self._value = parse_card_value(card_value_key)
        card_suit = card_key[1]
        if card_suit not in suits:
            raise ValueError(f"invalid card suit {card_suit} in card key {card_key}")
        self._suit = card_suit

    @property
    def value(self) -> int:
        """The numerical value of this card."""
        return self._value

    @property
    def suit(self) -> int:
        """The suit of this card."""
        return self._suit

    def __eq__(self, __other: object) -> bool:
        """Checks if the numerical value of two cards is equal (suits are not checked)."""
        return self._value == __other._value

    def __lt__(self, __other: object) -> bool:
        """Checks if the numerical value of this card is less than another card (suits are not checked)."""
        return self._value < __other._value

class HandType(IntEnum):
    """Represents the type of a hand."""
    high_card = 1
    one_pair = 2
    two_pairs = 3
    three_of_a_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9
    royal_flush = 10

class Hand:
    """Represents a poker hand."""
    def __init__(self, cards: Iterable[Card]) -> None:
        """Create a poker hand from the list of cards."""
        self._cards = sorted(cards, reverse=True)
        self._value_histogram = self._generate_card_histogram(lambda card: card.value)
        self._pairs = ()
        self._triple = 0
        self._quadruple = 0
        self._remaining_cards = ()
        self._hand_type = HandType.high_card
        self._determine_hand_type()

    def _determine_hand_type(self) -> None:
        """Determine the type of poker hand this is."""
        is_flush = self._is_flush()
        is_straight = self._is_straight()
        if is_flush and is_straight:
            if self._cards[0].value == 14:
                self._hand_type = HandType.royal_flush
                return
            self._hand_type = HandType.straight_flush
            return
        if is_flush:
            self._hand_type = HandType.flush
            return
        if is_straight:
            self._hand_type = HandType.straight
            return
        pairs = []
        triple = 0
        quadruple = 0
        remaining_cards = []
        for value, count in self._value_histogram.items():
            if count == 1:
                remaining_cards.append(value)
            elif count == 2:
                pairs.append(value)
            elif count == 3:
                triple = value
            else:
                quadruple = value
        pairs.sort(reverse=True)
        self._pairs = tuple(pairs)
        self._triple = triple
        self._quadruple = quadruple
        remaining_cards.sort(reverse=True)
        self._remaining_cards = tuple(remaining_cards)
        if self._quadruple != 0:
            self._hand_type = HandType.four_of_a_kind
            return
        if self._triple != 0:
            if len(self._pairs) == 1:
                self._hand_type = HandType.full_house
                return
            self._hand_type = HandType.three_of_a_kind
            return
        if len(self._pairs) == 2:
            self._hand_type = HandType.two_pairs
            return
        if len(self._pairs) == 1:
            self._hand_type = HandType.one_pair
            return

    def _generate_card_histogram(self, attribute_lambda: Callable[[Card], Any]) -> dict[int, int]:
        """Generates frequency map of a card attribute in this hand."""
        attribute_histogram = {}
        for attribute in map(attribute_lambda, self._cards):
            attribute_count = attribute_histogram.get(attribute)
            if attribute_count is None:
                attribute_count = 0
            attribute_count += 1
            attribute_histogram[attribute] = attribute_count
        return attribute_histogram

    def _is_flush(self) -> bool:
        """Determine if the hand is a flush."""
        for i in range(0, len(self._cards) - 1):
            suit_a = self._cards[i].suit
            suit_b = self._cards[i + 1].suit
            if suit_a != suit_b:
                return False
        return True

    def _is_straight(self) -> bool:
        """Determine if the hand is a straight."""
        for i in range(0, len(self._cards) - 1):
            value_a = self._cards[i].value
            value_b = self._cards[i + 1].value
            if value_a != value_b + 1:
                return False
        return True

    def __lt__(self, __other: object) -> bool:
        """
        Check if this hand is of lower value than the other hand.

        Currently it is assumed that ties won't happen.
        """
        if self._hand_type != __other._hand_type:
            return self._hand_type < __other._hand_type
        match self._hand_type:
            case HandType.straight_flush | HandType.straight | HandType.flush | HandType.high_card:
                for i in range(len(self._cards)):
                    card_a_value = self._cards[i].value
                    card_b_value = __other._cards[i].value
                    if card_a_value != card_b_value:
                        return card_a_value < card_b_value
            case HandType.four_of_a_kind:
                quadruple_value_a = self._quadruple
                quadruple_value_b = __other._quadruple
                return quadruple_value_a < quadruple_value_b
            case HandType.full_house | HandType.three_of_a_kind:
                triple_value_a = self._triple
                triple_value_b = __other._triple
                return triple_value_a < triple_value_b
            case HandType.two_pairs | HandType.one_pair:
                for i in range(len(self._pairs)):
                    pair_value_a = self._pairs[i]
                    pair_value_b = __other._pairs[i]
                    if pair_value_a != pair_value_b:
                        return pair_value_a < pair_value_b
        for i in range(len(self._remaining_cards)):
            card_a_value = self._remaining_cards[i]
            card_b_value = __other._remaining_cards[i]
            if card_a_value != card_b_value:
                return card_a_value < card_b_value

    def __gt__(self, __other: object) -> bool:
        """
        Check if this hand is of higher value than the other hand.

        Currently it is assumed that ties won't happen.
        """
        return not self < __other