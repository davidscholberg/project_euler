def pythagorean_triplets(int n) -> tuple[tuple[int, int, int]]:
    """All pythagorean triplets whose sum equals n."""
    triplets = []
    cdef int a, b, c = 0
    for a in range(1, (n // 3) + 1):
        for b in range(a + 1, (n // 2) + 1):
            c = n - a - b
            if (a ** 2) + (b ** 2) == c ** 2:
                triplets.append((a, b, c))
    return tuple(triplets)

def is_pythagorean_triplet(triplet: tuple[int, int, int]) -> bool:
    return (triplet[0] ** 2) + (triplet[1] ** 2) == triplet[2] ** 2