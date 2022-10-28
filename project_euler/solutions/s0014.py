from project_euler.util.sequences.collatz import Collatz

def get_answer() -> int:
    collatz = Collatz()
    input_length_pairs = map(lambda n: (n, collatz.sequence_length(n)), range(1, 1000000))
    return max(input_length_pairs, key=lambda n: n[1])[0]