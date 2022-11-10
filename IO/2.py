data1 = open("tiepcr.rtf", mode="r")
lines = data1.readlines()
data2 = open("new_tiepcr.rtf", mode="w")
i = 0
for line in lines:
    if i == 4:
        i += 1
        continue
    else:
        data2.write(line)
    i += 1

"""
ko in duoc anh em gt ho cai la sao d in dc the
lines1=data2.readlines()
print(lines1)
"""

