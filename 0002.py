def get_sum_of_even_fibonacci_numbers_capped(cap):
    if cap < 2:
        return 0
    previous_previous = 1
    previous = 2
    current = 3
    sum_of_even_fibonacci_numbers = 2
    while current <= cap:
        if current % 2 == 0:
            sum_of_even_fibonacci_numbers += current
        previous_previous = previous
        previous = current
        current = previous_previous + previous
    return sum_of_even_fibonacci_numbers

answer = get_sum_of_even_fibonacci_numbers_capped(4000000)
print(answer)
