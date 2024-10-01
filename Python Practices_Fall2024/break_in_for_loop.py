monthly_sales = [42, 30, 39, 40, 45, 12]
months = ['jan', 'feb', 'Mar', 'Apr', 'May', 'june']

threshold = 35
'''
for sales_amount in monthly_sales:
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than threshold")
       # break
    else:
        print(f"Sales amount {sales_amount} is greater than threshold")
'''
for sales_amount, month in zip(monthly_sales, months):
    # print(month, sales_amount)
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than threshold in {month}")
       # break
    else:
        print(f"Sales amount {sales_amount} is greater than threshold in {month}")