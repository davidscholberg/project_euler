from project_euler.util.sequences.cyclical_figurates import cyclical_figurates
from project_euler.util.sequences.heptagonal_numbers import is_heptagonal_number
from project_euler.util.sequences.hexagonal_numbers import is_hexagonal_number
from project_euler.util.sequences.octagonal_numbers import is_octagonal_number
from project_euler.util.sequences.pentagonal_numbers import is_pentagonal_number
from project_euler.util.sequences.square_numbers import is_square_number
from project_euler.util.sequences.triangle_numbers import is_triangle_number

def get_answer() -> int:
    figurate_tests = (
        is_triangle_number,
        is_square_number,
        is_pentagonal_number,
        is_hexagonal_number,
        is_heptagonal_number,
        is_octagonal_number
    )
    return sum(cyclical_figurates(figurate_tests))