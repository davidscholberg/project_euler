from unittest import TestCase

from project_euler.util.dates.month import days_in_month

class TestMonth(TestCase):
    def test_days_in_month(self):
        self.assertEqual(31, days_in_month(1, 2022))
        self.assertEqual(28, days_in_month(2, 2022))
        self.assertEqual(31, days_in_month(3, 2022))
        self.assertEqual(30, days_in_month(4, 2022))
        self.assertEqual(31, days_in_month(5, 2022))
        self.assertEqual(30, days_in_month(6, 2022))
        self.assertEqual(31, days_in_month(7, 2022))
        self.assertEqual(31, days_in_month(8, 2022))
        self.assertEqual(30, days_in_month(9, 2022))
        self.assertEqual(31, days_in_month(10, 2022))
        self.assertEqual(30, days_in_month(11, 2022))
        self.assertEqual(31, days_in_month(12, 2022))
        self.assertEqual(29, days_in_month(2, 2024))