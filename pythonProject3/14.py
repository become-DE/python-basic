str1 = "Apple"
dic=dict()
for char in str1:
    count=str1.count(char)
    dic[char]=count
print(dic)