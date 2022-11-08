import math

def factorial(n: int, cache: None | dict = None) -> int:
    if cache is not None:
        if n in cache:
            return cache[n]
        if n == 0:
            cache[n] = 1
            return 1
        result = n * factorial(n - 1, cache=cache)
        cache[n] = result
        return result
    return math.prod(range(2, n + 1))