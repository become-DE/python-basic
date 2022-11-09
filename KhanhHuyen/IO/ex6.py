file1 = open('test.txt','r')
lines = file1.readlines()
N = len(lines)
file2 = open('new_file.txt', 'w')
for i in range(N):
    if i == 4:
        continue
    file2.writelines(lines[i])


file1.close()
file2.close()
