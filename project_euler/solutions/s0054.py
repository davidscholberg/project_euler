from project_euler.paths import data_file_path
from project_euler.util.games.poker import Card, Hand

def get_answer() -> int:
    with open(data_file_path('2_player_poker_games.txt')) as file:
        player_1_wins = 0
        for line in file:
            card_keys = line.split()
            hand_1 = Hand(map(Card, card_keys[:5]))
            hand_2 = Hand(map(Card, card_keys[5:]))
            if hand_1 > hand_2:
                player_1_wins += 1
        return player_1_wins