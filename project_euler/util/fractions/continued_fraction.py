from typing import Callable, Iterator

from project_euler.util.fractions.add import add_fractions

class ContinuedFraction:
    """Encapsulates continued fraction calculation."""
    def __init__(self, get_a_terms: Callable[[], Iterator[int]], get_b_terms: Callable[[], Iterator[int]], starting_cache_depth: int = -1) -> None:
        """
        Creates a continued fraction object.

        The terms parameters are functions that produce unique iterators for
        all of the a and b terms in the continued fraction. Ideally the produced
        iterators are all infinite.

        The form of a continued fraction as it relates to the terms is as follows:

        b0 + (a0 / (b1 + (a1 / (b2 + (...)))))

        The starting_cache_depth parameter specifies the depth from the top
        where we can start caching values of deeper iteration. This should only
        be used if the a and b terms repeat after the starting cache depth.
        """
        self._get_a_terms = get_a_terms
        self._get_b_terms = get_b_terms
        self._cache: dict[int, tuple[int, int]] = {}
        self._starting_cache_depth = starting_cache_depth
        self._starting_depth = 0

    def calculate(self, depth: int) -> tuple[int, int]:
        """
        Returns the value of this continued fraction to the given depth. The
        returned fraction is reduced.
        """
        a_terms = self._get_a_terms()
        b_terms = self._get_b_terms()
        self._starting_depth = depth
        return self._calculate(a_terms, b_terms, depth=depth)

    def _calculate(self, a_terms: Iterator[int], b_terms: Iterator[int], depth: int = 0) -> tuple[int, int]:
        """
        Internal method for recursively calculating this continued fraction at
        the given depth.
        """
        depth_is_cacheable = self._depth_is_cacheable(depth)
        if depth_is_cacheable:
            cache_result = self._cache.get(depth)
            if cache_result is not None:
                return cache_result
        a_n = next(a_terms)
        b_n = next(b_terms)
        if depth == 0:
            b_n_plus_1 = next(b_terms)
            result = add_fractions((b_n, 1), (a_n, b_n_plus_1))
            if depth_is_cacheable:
                self._cache[depth] = result
            return result
        (result_numerator, result_denominator) = self._calculate(a_terms, b_terms, depth=depth - 1)
        result = add_fractions((b_n, 1), (a_n * result_denominator, result_numerator))
        if depth_is_cacheable:
            self._cache[depth] = result
        return result

    def _depth_is_cacheable(self, depth: int) -> bool:
        """Tells whether the current depth is cacheable."""
        if self._starting_cache_depth == -1:
            return False
        return depth <= self._starting_depth - self._starting_cache_depth