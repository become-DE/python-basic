numbers = [12, 75, 150, 180, 145, 525, 50]
res = []
for x in numbers:
    if x > 500:
        break
    elif (x % 5 == 0) & (x <= 150):
        res.append(x)

print(*res, sep='\n')
