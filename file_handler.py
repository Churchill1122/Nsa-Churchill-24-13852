def save_expense(expense):
    with open("expenses.txt", "a") as file:
        file.write(
            f"{expense['amount']},{expense['category']},{expense['description']}\n"
        )


def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, description = line.strip().split(",")
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })
    except FileNotFoundError:
        pass
    return expenses
