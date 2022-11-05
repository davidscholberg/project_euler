from itertools import takewhile
from typing import Any, Iterable, Iterator

from project_euler.util.arithmetic.polynomial import polynomial
from project_euler.util.primes.is_prime import is_prime

def polynomial_primes(coefficients: Iterable[Any], inputs: Iterable[Any]) -> Iterator[Any]:
    yield from takewhile(is_prime, polynomial(coefficients, inputs))