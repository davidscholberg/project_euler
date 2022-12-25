from project_euler.util.sequences.pentagonal_numbers import pentagonal_numbers

def get_answer() -> int:
    pentagonal_number_list = []
    pentagonal_number_iterator = pentagonal_numbers()
    pentagonal_number_list.append(next(pentagonal_number_iterator))
    pentagonal_number_list.append(next(pentagonal_number_iterator))
    pentagonal_pair = None
    pair_difference = lambda t: abs(t[0] - t[1])
    pair_sum = lambda t: t[0] + t[1]
    largest_pentagonal_gap = lambda: pentagonal_number_list[-1] - pentagonal_number_list[-2]
    while True:
        if pentagonal_pair is not None and pair_difference(pentagonal_pair) < largest_pentagonal_gap():
            break
        for i in range(0, len(pentagonal_number_list) - 1):
            pentagonal_1 = pentagonal_number_list[i]
            pentagonal_2 = pentagonal_number_list[-1]
            difference = abs(pentagonal_1 - pentagonal_2)
            if 