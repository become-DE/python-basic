income = int(input())
if income <= 10000:
    tax = 0
    print(tax)
elif income <= 20000:
    tax = (income - 10000) * 0.1
    print(tax)
else:
    tax = (income-20000) * 0.2 +  10000*0.1
    print(tax)