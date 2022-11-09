str_x="Emma is good deverloper. Emma is a writer"
n = len(str_x)
count = 0
m = 0
for i in range(0, n):
    if str_x[i] ==' ':
        str_cut = str_x[m:i]
        if str_cut == "Emma":
            count = count + 1
        m = i + 1
print(count)
