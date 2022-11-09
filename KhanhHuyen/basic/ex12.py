income = int(input())
if income <= 10000:
    tax = 0
else:
    income = income - 10000
    if income <= 10000:
        tax = income * 0.1
    else: 
        tax = 10000 * 0.1 + (income - 10000) * 0.2
    
print(tax)