from project_euler.util.sequences.pentagonal_numbers import pentagonal_numbers, is_pentagonal_number

def get_answer() -> int:
    pentagonal_number_list = []
    pentagonal_number_iterator = pentagonal_numbers()
    pentagonal_number_list.append(next(pentagonal_number_iterator))
    pentagonal_number_list.append(next(pentagonal_number_iterator))
    while True:
        for i in range(len(pentagonal_number_list) - 2, -1, -1):
            pentagonal_1 = pentagonal_number_list[-1]
            pentagonal_2 = pentagonal_number_list[i]
            pentagonal_sum = pentagonal_1 + pentagonal_2
            if not is_pentagonal_number(pentagonal_sum):
                continue
            pentagonal_difference = pentagonal_1 - pentagonal_2
            if not is_pentagonal_number(pentagonal_difference):
                continue
            return pentagonal_difference
        pentagonal_number_list.append(next(pentagonal_number_iterator))