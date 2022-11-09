list1=[10, 20, 25, 30, 35]
list2=[40, 45, 60, 75, 90]
list = [0] * 5
j = 0
for i in range(5):
    if list1[i] % 2 != 0:
        list[j] = list1[i]
        j+=1
for i in range(5):
    if list2[i] % 2 == 0:
        list[j] = list2[i]
        j+=1
print("result list:", list)
