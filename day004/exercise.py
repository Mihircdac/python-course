# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

# Assignment/Exercises 
# Topics covered : Modules,Functions,Looping,Conditional constructs,Input,Output,Collections :
# ---------------------------------------------------------------------------------------------------------
# 1.1) Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user 
# for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania is provided by the user 

# Operations supported by our program are :
#   1:  Display all the elements in the members list
#   2:  Add an element to the members collection like 'Sehwag' 
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection 
#   6:  Display third, fourth and fifth element from the collection 

# Keep asking the user for the operation in this store untill he chooses to exit from the program

# Sample code template for my_list_store starts

def list_display_members(members) :
    print(members)    

def list_add_element(members) :
    print(members)
    element=input("enter your name to the list: ")
    members.append(element)
    
    

def list_add_elements(members):
    #while 
    
    # cnt = 1
    # num = int(input("Enter number"))
    # while cnt <= num:
    #     element=input("Enter name: ")  
    #     members.extend([element])
    #     cnt += 1 
    # print(members)  
    #  ----------------------#
    
    #in for loop -----------
    num = int(input("Enter number:"))
    name = input("Enter name:")
    nam = [name]
    for i in range(0, num,1):
        members.extend(nam)
        # members = members.extend(["Enter name:"])
        print(members)
    
        
    
    
def list_remove_element(members):
    members.pop(int(input("enter the index number: ")))
    print(members)
   

def remove_last_element(members) :
    members.pop()
    print("updated list is: ", members)

def display_3_4_5_element(members):
	print(members[3:6:1])

			
def my_list_store():
    print("\n Welcome to Our List Store !!! ")
    print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    
    # Write code to populate the members collection with list of names
    how_many_people=int(input("enter people: "))
    members=[]
    for i in range(0,how_many_people,1):
            members.append(input("members"))
    
    

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display all elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members(members) 
        elif choice ==2:
            list_add_element(members) 
        elif choice ==3:
            list_add_elements(members)
        elif choice ==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_list_store()		
# Sample code template for my_list_store ends