from libcpp.vector cimport vector
from typing import Iterator

def permutations(int n, int choose = -1) -> Iterator[tuple[int]]:
    """Permutations of numbers 0 through n - 1, optionally limited to choose elements.

    Note that if choose is not specified or equals n, the results will be in lexicographic order. If
    choose is less than n, the results will not be in lexicographic order."""
    if choose == -1:
        choose = n
    if choose == 1:
        yield from map(tuple, range(0, n))
        return
    cdef vector[int] sequence = range(0, choose)
    while True:
        while True:
            yield tuple(sequence)
            if not next_permutation(sequence):
                break
        if not next_set_for_permutation(sequence, n, choose):
            break

# https://www.techiedelight.com/find-permutations-string-cpp-java-iterative/
cdef bint next_permutation(vector[int]& sequence):
    """Sets sequence to next lexicographic permutation."""
    cdef int n = sequence.size()
    cdef int i, j
    i = n - 1
    while sequence[i - 1] >= sequence[i]:
        i -= 1
        if i == 0:
            reverse(sequence, 0, n - 1)
            return False
    j = n - 1
    while j > i and sequence[j] <= sequence[i - 1]:
        j -= 1
    swap(sequence, i - 1, j)
    reverse(sequence, i, n - 1)
    return True

# https://stackoverflow.com/a/64039677
cdef bint next_set_for_permutation(vector[int]& sequence, int n, int choose):
    """Sets sequence to next set to permute."""
    cdef int i, j
    for i in range(choose - 1, -1, -1):
        if sequence[i] < n - choose + i:
            sequence[i] += 1
            for j in range(i + 1, choose):
                sequence[j] = sequence[j - 1] + 1
            return True
    return False

cdef void swap(vector[int]& sequence, int i, int j):
    cdef int a = sequence[i]
    sequence[i] = sequence[j]
    sequence[j] = a

cdef void reverse(vector[int]& sequence, int i, int j):
    while i < j:
        swap(sequence, i, j)
        i += 1
        j -= 1