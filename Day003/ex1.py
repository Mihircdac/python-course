# 1) Take a number from the user and print sum from 1 to that number 

# num=int(input("enter the number: "))

# var_1=0
# cnt=1

# while cnt<=num:
#     var_1+=cnt
#     print(var_1)
#     cnt+=1


#do while

# num=int(input("enter the number: "))
# var_1=0
# cnt=1

# while True:
#     var_1 += cnt
#     cnt += 1
#     if cnt > num:
#         break
# print(var_1)

#for loops

#3) Take a number from the user and calculate the sum of all even from 1 to that number

num=int(input("enter the number: "))
sum = 0


for cnt in range(1,num+1,1):
    if  cnt % 2 == 0:
         sum += cnt
print("sum is ",sum)




    

    

        