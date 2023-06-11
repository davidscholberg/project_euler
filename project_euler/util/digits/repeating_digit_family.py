from itertools import islice, product

from project_euler.util.digits.digits import digits, number_from_digits

def build_repeating_digit_family(key: str) -> tuple[int]:
    """
    Builds and returns a repeating digit family from the given key.

    A repeating digit family is a set of n-digit numbers that can be transformed
    into eachother by changing one or more repeating digits into a different
    repeating digit.

    See get_repeating_digit_family_keys for an expanation of the key structure.
    """
    base_digits = tuple(map(lambda s: s if s == "X" else int(s), key))
    replacement_indices = tuple(
        map(
            lambda t: t[0],
            filter(
                lambda t: t[1] == "X",
                enumerate(key)
            )
        )
    )
    family = []
    starting_digit = 0
    if replacement_indices[0] == 0:
        starting_digit = 1
    for replacement_digit in range(starting_digit, 10):
        digits_list = list(base_digits)
        for replacement_index in replacement_indices:
            digits_list[replacement_index] = replacement_digit
        family.append(number_from_digits(digits_list))
    return tuple(family)

def get_repeating_digit_family_keys(n: int) -> tuple[str]:
    """
    Builds and returns a list of repeating digit family keys based on the given
    number.

    A repeating digit family key is a string that represents the blueprint for
    generating a repeating digit family. "5XX4" is a key specifying that the X
    values are meant to be substituted with repeating digits.
    """
    digit_to_indices_map = {}
    n_digits = digits(n)
    repeating_digit_family_keys = []
    for i, digit in enumerate(n_digits):
        indices = digit_to_indices_map.get(digit, [])
        indices.append(i)
        if len(indices) == 1:
            digit_to_indices_map[digit] = indices
    repeat_count_to_arrangement_map = {}
    for digit, indices in digit_to_indices_map.items():
        repeat_count = len(indices)
        digit_arrangements = repeat_count_to_arrangement_map.get(repeat_count)
        if digit_arrangements is None:
            digit_arrangements = tuple(islice(product(("O", "X"), repeat=repeat_count), 1, None))
            repeat_count_to_arrangement_map[repeat_count] = digit_arrangements
        for digit_arrangement in digit_arrangements:
            digits_list = list(n_digits)
            for arrangement_index, digit_index in enumerate(indices):
                if digit_arrangement[arrangement_index] == "X":
                    digits_list[digit_index] = "X"
            repeating_digit_family_keys.append(''.join(map(str, digits_list)))
    return tuple(repeating_digit_family_keys)