from unittest import TestCase

from project_euler.util.dates.year import days_in_year, is_leap_year

class TestYear(TestCase):
    def test_days_in_year(self):
        self.assertEqual(366, days_in_year(2000))
        self.assertEqual(365, days_in_year(1900))
        self.assertEqual(366, days_in_year(2004))
        self.assertEqual(365, days_in_year(1955))

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(1200))
        self.assertFalse(is_leap_year(1000))
        self.assertTrue(is_leap_year(1836))
        self.assertFalse(is_leap_year(1493))