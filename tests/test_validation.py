import unittest
from validation import parse_amount, parse_date

class ValidationTests(unittest.TestCase):
    def test_amount_to_minor_units(self): self.assertEqual(parse_amount("12.34"), 1234)
    def test_reject_invalid_amounts(self):
        for value in ("0", "-1", "1.234", "NaN", "abc"):
            with self.subTest(value=value), self.assertRaises(ValueError): parse_amount(value)
    def test_date(self): self.assertEqual(parse_date("2026-02-03"), "2026-02-03")
    def test_reject_bad_date(self):
        with self.assertRaises(ValueError): parse_date("03/02/2026")
