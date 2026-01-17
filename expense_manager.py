def create_expense(amount, category, description):
    return {
        "amount": amount,
        "category": category,
        "description": description
    }


def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total
