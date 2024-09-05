l1=[10,20,30,40,50,66,77]
l2=list[10,20,30,40,50,66,77]


print(l1[3:7])

print(l1[1:6:1]) #if l2 error

#updation

l1[0]=30
print(l1)

l1[0:2:2]=[22]
print(l1)


l1.append(33)
print(l1)

l1.append("hello")
print(l1)

l1.extend([12,13,14])
print(l1)
 
l1.insert(9,100)
print(l1)

l1.remove("hello")
print(l1)

print(100 in l1)

l1.pop(1)
print(l1)

print(100 not in l1)

l1_copy=l1
print(id(l1))
print(id(l1_copy))

l1_copy=l1.copy()
print(id(l1))
print(id(l1_copy))
print(l1,l1_copy)

print("minimum value: ", min(l1),"and the maximun value is:  ",max(l1))

print("lenght is : ",len(l1))
 
print("count is : ",l1.count(100))



print("index is: ",l1.index(100))

print(l1.reverse())
print(l1)


