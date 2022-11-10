def add(num):
    if num > 0 :
        return num+add(num-1)
    else:
        return 0
rec = add(10)
print(rec)