import json
import tempfile
import unittest
from pathlib import Path
from model import Transaction
from storage import load_transactions, save_transactions

class StorageTests(unittest.TestCase):
    def test_round_trip_and_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "transactions.json"
            self.assertEqual(load_transactions(path), [])
            expected = [Transaction("income", "Salary", 12500)]
            save_transactions(expected, path)
            self.assertEqual(load_transactions(path), expected)
    def test_corrupt_file_returns_empty(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "transactions.json"
            path.write_text("{broken", encoding="utf-8")
            self.assertEqual(load_transactions(path), [])
    def test_migrates_legacy_record(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "transactions.json"
            path.write_text(json.dumps([{"type":"expense", "category":"Food", "amount":100, "note":""}]), encoding="utf-8")
            loaded = load_transactions(path)
            self.assertEqual(len(loaded), 1)
            self.assertTrue(loaded[0].transaction_id)
