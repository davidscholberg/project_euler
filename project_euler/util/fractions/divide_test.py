from unittest import TestCase

from project_euler.util.fractions.divide import divide

class TestDivide(TestCase):
    def test_divide(self):
        self.assertEqual(
            (
                '1',
                '0.5',
                '0.(3)',
                '0.25',
                '0.2',
                '0.1(6)',
                '0.(142857)',
                '0.125',
                '0.(1)',
                '0.1'
            ),
            tuple(map(
                lambda n: str(divide(1, n)),
                range(1, 11)
            ))
        )
        self.assertEqual('2', str(divide(4, 2)))
        self.assertEqual('1.5', str(divide(3, 2)))