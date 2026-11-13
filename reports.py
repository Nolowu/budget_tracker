from datetime import date

def filter_transactions(transactions, kind=None, category=None, on_date=None, minimum=None, maximum=None):
    if on_date:
        try: on_date = date.fromisoformat(on_date).isoformat()
        except ValueError: raise ValueError("Date must use YYYY-MM-DD format.")
    category_key = category.casefold() if category else None
    result = []
    for t in transactions:
        if kind and t.type != kind: continue
        if category_key and t.category.casefold() != category_key: continue
        if on_date and t.transaction_date != on_date: continue
        if minimum is not None and t.amount < minimum: continue
        if maximum is not None and t.amount > maximum: continue
        result.append(t)
    return result

