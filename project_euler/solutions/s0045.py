from project_euler.util.sequences.hexagonal_numbers import hexagonal_numbers
from project_euler.util.sequences.pentagonal_numbers import is_pentagonal_number
from project_euler.util.sequences.triangle_numbers import is_triangle_number

def get_answer() -> int:
    hexagonal_number_iterator = hexagonal_numbers()
    while next(hexagonal_number_iterator) != 40755:
        pass
    for hexagonal_number in hexagonal_number_iterator:
        if is_pentagonal_number(hexagonal_number) and is_triangle_number(hexagonal_number):
            return hexagonal_number
    return 0