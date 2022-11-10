lst1=[10,20,25,30,35]
lst2=[40,45,60,75,80]
rsodd=[]
rseven=[]
for i in lst1 :
    if i%2==0 :
        rsodd.append(i)
    else:
        rseven.append(i)
for i in lst2 :
    if i%2==0 :
        rsodd.append(i)
    else:
        rseven.append(i)
print(rsodd)
print(rseven)