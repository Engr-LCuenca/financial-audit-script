from __future__ import annotations

from typing import TypedDict, List


class Transaction(TypedDict):
    id: int
    client: str
    amount: float
    status: str


def load_transactions() -> List[Transaction]:
    """Simulate a list of 10 financial transactions for auditing."""
    return [
        {"id": 101, "client": "Alice", "amount": 120.50, "status": "approved"},
        {"id": 102, "client": "Bob", "amount": 75.00, "status": "pending"},
        {"id": 103, "client": "Carol", "amount": 250.00, "status": "approved"},
        {"id": 104, "client": "David", "amount": 40.25, "status": "rejected"},
        {"id": 105, "client": "Eva", "amount": 890.00, "status": "approved"},
        {"id": 106, "client": "Frank", "amount": -15.75, "status": "flagged"},
        {"id": 107, "client": "Grace", "amount": 320.10, "status": "approved"},
        {"id": 108, "client": "Hank", "amount": 60.00, "status": "pending"},
        {"id": 109, "client": "Ivy", "amount": 500.00, "status": "approved"},
        {"id": 110, "client": "Jack", "amount": -200.00, "status": "flagged"},
    ]


def filter_suspicious_orders(transactions: List[Transaction], limit: float) -> List[Transaction]:
    """Return a new list with orders above the limit or with negative amounts."""
    suspicious_orders: List[Transaction] = []

    # Loop through each transaction and keep the ones that look suspicious.
    for transaction in transactions:
        amount = transaction["amount"]
        if amount < 0 or amount > limit:
            suspicious_orders.append(transaction)

    return suspicious_orders


def calculate_total_tax(transactions: List[Transaction]) -> float:
    """Apply a simulated 8% tax only to valid positive amounts."""
    total_tax = 0.0

    # Loop through the filtered list and accumulate tax for valid amounts.
    for transaction in transactions:
        amount = transaction["amount"]
        if amount >= 0:
            total_tax += amount * 0.08

    return round(total_tax, 2)


if __name__ == "__main__":
    transactions = load_transactions()
    suspicious_orders = filter_suspicious_orders(transactions, 300.0)
    total_tax = calculate_total_tax(suspicious_orders)

    print("Loaded transactions:", len(transactions))
    print("Suspicious orders:", suspicious_orders)
    print("Total tax:", total_tax)
