list1 = [ 10, 20, 25, 30, 35]
list2 = [ 40, 45, 60, 75, 90]
res = list()
res.extend([x for x in list1 if x % 2 == 1])
res.extend([x for x in list2 if x % 2 == 0])

print(res)