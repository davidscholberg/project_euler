from math import factorial, prod

def n_choose_k(n: int, k: int) -> int:
    """Return the number of ways to choose k items from n."""
    term_a = k
    term_b = n - k
    terms = (term_a, term_b)
    term_to_cancel = max(terms)
    term_to_compute = min(terms)
    top_term = prod(range(n, term_to_cancel, -1))
    return top_term // factorial(term_to_compute)