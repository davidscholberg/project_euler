import math

def get_pythagorean_triplet_that_sums_to_n(n: int) -> tuple:
    for a in range(1, n // 3):
        for b in range(a + 1, (n // 2)):
            c = n - a - b
            if c <= b:
                break
            if (a ** 2) + (b ** 2) == c ** 2:
                return (a, b, c)
    return (0,)

answer = math.prod(get_pythagorean_triplet_that_sums_to_n(1000))
print(answer)