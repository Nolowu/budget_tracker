from dataclasses import dataclass

@dataclass
class Transaction:
    type: str        # "income" or "expense"
    category: str    # "food", "rent", "salary"...
    amount: int      # stored in cents (kobo), not decimals
    note: str = ""