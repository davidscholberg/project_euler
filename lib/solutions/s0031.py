from ..util.sums import CombinationsOfNumbersThatSumToN

def get_answer() -> int:
    return sum(map(lambda c: 1, CombinationsOfNumbersThatSumToN((1, 2, 5, 10, 20, 50, 100, 200), 200)))