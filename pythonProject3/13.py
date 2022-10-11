str1 = "PYnative29@#8496"
x = 0
y = 0
for num in str1:
    if num.isnumeric():
        x+=int(num)
        y+=1
avg=x/y
print(x,'and' ,avg)
