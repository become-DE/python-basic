str1="ault"
str2="kelly"
def append(str1,str2):
    midstr1=int(len(str1)/2)
    x = str1[:midstr1]
    x = x + str2
    x= x+str1[midstr1:]
    print(x)
append("ault","kelly")