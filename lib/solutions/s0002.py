from ..util.sequences import FibonacciIterator

def get_sum_of_even_fibonacci_numbers_capped(cap):
    sum_of_even_fibonacci_numbers = 0
    for term in FibonacciIterator(cap):
        if term % 2 == 0:
            sum_of_even_fibonacci_numbers += term
    return sum_of_even_fibonacci_numbers

def get_answer() -> int:
    return get_sum_of_even_fibonacci_numbers_capped(4000000)