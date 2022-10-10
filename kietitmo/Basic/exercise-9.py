import math
from pickle import TRUE
number = input("enter number: ")
str_number = str(number)
bool_res = TRUE

for x in range(math.ceil(len(str_number)/2)):
    if str_number[x] != str_number[-x-1]:
        bool_res = False
        break
    
if bool_res:
    print("Yes")
else:
    print("No")
