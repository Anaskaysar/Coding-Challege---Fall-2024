expenses = [1000, 2000, 3000, 4000, 6000]

total_expense = 0

for expense in expenses:
    total_expense = total_expense+expense
print(total_expense)

'''
for i in range(len(expenses)):
    expense = expenses[i]
    print(f"Month {i+1}, Expense: {expense}")

'''
for i, expense in enumerate(expenses):
    print(f"Month {i+1}, Expense: {expense}")