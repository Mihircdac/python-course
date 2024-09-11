# -- exceptions link for reference
# https://docs.python.org/3/library/exceptions.html

# ------------------------------------------------
# Exercise : Exceptions
# -------------------------------------------------

# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )
# color = {}
# for i in (0,3,1):
#     no = int(input("enter key"))
#     col = input("Enter color")
#     color[no] = col
# print(color)   


# try:  
#     key = int(input("Enter key:"))    
#     if(key != color[key]):
#        print("color is found")
# except Exception:
#         key =  int(input("Enter the key again: "))  
#         print("color not found")

    

# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 

li = []
for i in range(0,5,1):
    names = input("Enter the names:")
    li.append(names)
print(li)  

try:
    index = int(input("enter the index value"))
    print(li[index])
except Exception:
    print("invalid index")




# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)