from operator import indexOf


fin= open("./kietitmo/IO/test.txt","r")
fout = open("./kietitmo/IO/new_file.txt","w")

f = fin.readlines()
f.pop(4)

for x in f:
    fout.write(x)