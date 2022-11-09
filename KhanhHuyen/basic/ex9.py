str = input()
n = len(str)
check = 1
for i in range(0, round(n/2)):
    if str[i] != str[n - i - 1]:
        check = 0
        break
if check == 1:
    print(str, "is a palindrom number")
else:
    print(str, "is not a palindrom number")


