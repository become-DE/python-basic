str = input("enter string: ")
print("Original String is: ", str)

print("Printing only even index chars")
for x in range(len(str)):
    if x % 2 == 0 :
        print(str[x])
