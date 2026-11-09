def totals_by_category(transactions, kind):
    totals = {}
    for t in transactions:
        if t.type == kind:
            totals[t.category] = totals.get(t.category, 0) + t.amount
    return totals


def total(transactions, kind):
    return sum(t.amount for t in transactions if t.type == kind)


def balance(transactions):
    return total(transactions, "income") - total(transactions, "expense")