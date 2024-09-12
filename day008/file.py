m=open("ogfile.txt",'r+')
list=[]
for line in m:
    list.append(line.strip() + "Pune")

print([list])
m.close()

m=open("ogfile.txt",'w+')
for line in list:
    list.write(line)