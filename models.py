# Forward legacy imports to the modular models package
from models import (
    db,
    User,
    Category,
    Expense,
    Income,
    Budget,
    SavingsGoal,
    RecurringExpense
)

__all__ = ['db', 'User', 'Category', 'Expense', 'Income', 'Budget', 'SavingsGoal', 'RecurringExpense']