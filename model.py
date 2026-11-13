from dataclasses import dataclass, field
from datetime import date
from uuid import uuid4

@dataclass
class Transaction:
    type: str
    category: str
    amount: int  # integer minor units (cents/kobo)
    note: str = ""
    transaction_id: str = field(default_factory=lambda: str(uuid4()))
    transaction_date: str = field(default_factory=lambda: date.today().isoformat())
