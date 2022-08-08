def get_smallest_natural_number_evenly_divisible_by_1_through_n(n: int) -> int:
    multiple_of_n = n
    while True:
        found = True
        for i in range(n - 1, 1, -1):
            if multiple_of_n % i != 0:
                found = False
                break
        if found:
            return multiple_of_n
        multiple_of_n += n

answer = get_smallest_natural_number_evenly_divisible_by_1_through_n(20)
print(answer)