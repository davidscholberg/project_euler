from project_euler.util.multiples.factors import amicable_numbers

def get_answer() -> int:
    return sum(amicable_numbers(1, 9999))