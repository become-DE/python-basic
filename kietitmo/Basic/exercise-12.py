taxable_income =[10000, 10000, 25000]
rate = [0, 10 ,20]
res = 0.0
for x in range(len(taxable_income)):
    res += taxable_income[x]*rate[x]/100

print("result: ", res)