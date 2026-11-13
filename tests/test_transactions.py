import unittest
from reports import filter_transactions
from model import Transaction
from transactions import create_transaction, delete_transaction

class TransactionTests(unittest.TestCase):
    def setUp(self): self.items = [Transaction("income", "Salary", 10000, transaction_date="2026-01-02"), Transaction("expense", "Food", 2500, transaction_date="2026-01-03")]
    def test_filter_by_type_category_date_amount(self):
        self.assertEqual(filter_transactions(self.items, "expense", "food", "2026-01-03", 2000, 3000), [self.items[1]])
    def test_filter_no_match(self): self.assertEqual(filter_transactions(self.items, category="rent"), [])
    def test_create_income_and_expense(self):
        income = create_transaction("income", "Salary", 125000, "Monthly pay", "2026-03-01")
        expense = create_transaction("expense", "Food", 2500, transaction_date="2026-03-02")
        self.assertEqual((income.type, income.amount, income.transaction_date), ("income", 125000, "2026-03-01"))
        self.assertEqual((expense.type, expense.category), ("expense", "Food"))
    def test_delete_by_id(self):
        item = create_transaction("expense", "Food", 100)
        items = [item]
        self.assertEqual(delete_transaction(items, item.transaction_id), item)
        self.assertEqual(items, [])
        self.assertIsNone(delete_transaction(items, "missing"))
