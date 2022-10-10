pat = str(2)
n = 5
res = 0
temp = ''
for x in range(1, n + 1):
    for y in range(1, x + 1):
        temp += pat
    res += int(temp)
    temp = ''

print(res)