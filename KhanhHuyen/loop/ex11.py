import math
from operator import truediv
def check(n):
    if n <= 1: return False
    for i in range(2, (int)(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            break
    return True
start = 25
end = 50
for i in range(start, end):
    if(check(i)):
        print(i)

