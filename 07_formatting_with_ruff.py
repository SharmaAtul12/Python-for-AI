import os


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))


# Ctrl + S -> will automatically format the code with ruff
# Ctrl + Shift + P -> will open the command palette, then type "Format Document" and select it to format the code with ruff