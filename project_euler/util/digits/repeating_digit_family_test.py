from unittest import TestCase

from project_euler.util.digits.repeating_digit_family import build_repeating_digit_family, get_repeating_digit_family_keys

class TestRepeatingDigitFamily(TestCase):
    def test_build_repeating_digit_family(self):
        self.assertEqual(build_repeating_digit_family("5XX4"), (5004, 5114, 5224, 5334, 5444, 5554, 5664, 5774, 5884, 5994))
        self.assertEqual(build_repeating_digit_family("XX4"), (114, 224, 334, 444, 554, 664, 774, 884, 994))

    def test_get_repeating_digit_family_keys(self):
        self.assertEqual(get_repeating_digit_family_keys(5224), ("X224", "52X4", "5X24", "5XX4", "522X"))
        self.assertEqual(get_repeating_digit_family_keys(123), ("X23", "1X3", "12X"))