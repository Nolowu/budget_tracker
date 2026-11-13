def totals_by_category(transactions, kind):
    totals = {}
    for transaction in transactions:
        if transaction.type == kind:
            totals[transaction.category] = totals.get(transaction.category, 0) + transaction.amount
    return totals

def total(transactions, kind):
    return sum(t.amount for t in transactions if t.type == kind)

def balance(transactions):
    return total(transactions, "income") - total(transactions, "expense")
