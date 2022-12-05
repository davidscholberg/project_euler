from libcpp.list cimport list

from project_euler.util.digits.digits cimport digits_c

cdef int[10] digit_factorial_map = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
"""Map of the factorials of each base-10 digit."""

def digit_factorial_sum(int n) -> int:
    """Sum of the factorial of each digit of n."""
    cdef int total = 0
    cdef int digit
    cdef list[int] digits_list
    digits_c(n, &digits_list)
    for digit in digits_list:
        total += digit_factorial_map[digit]
    return total