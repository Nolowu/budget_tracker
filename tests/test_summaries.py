import unittest
from model import Transaction
from summary import balance, total, totals_by_category

class SummaryTests(unittest.TestCase):
    def setUp(self): self.items = [Transaction("income", "Salary", 10000), Transaction("expense", "Food", 2500), Transaction("expense", "Food", 500)]
    def test_totals_and_balance(self):
        self.assertEqual(total(self.items, "income"), 10000)
        self.assertEqual(total(self.items, "expense"), 3000)
        self.assertEqual(balance(self.items), 7000)
    def test_category_totals(self): self.assertEqual(totals_by_category(self.items, "expense"), {"Food": 3000})
