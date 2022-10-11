str1 = "PyNaTive"
up=[]
low=[]
for char in str1:
    if char.islower():
        low.append(char)
    else:
        up.append(char)
str2="".join(low+up)
print(str2)