from .import Expense

 expenses = Expenses.Expenses()
 expenses.read_expenses('data/spending_data.csv')

 spending_categories = []
 for expenses in expenses.list:
     spending_categories.append(expense.category)