
# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user 

# for ex: 
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user

# Operations supported by our program are :
# 	1: Union
# 	2: Intersection 
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B 
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A

# Sample code template for my set store
def set_union(setA,setB) :
    print('the union is; ', setA.union(setB))
    print(setA)
    
def set_intersection(setA,setB) :
    print("the intersection of a to b is: ", setA.intersection(setB))
    print(setA) 

def set_minus(setA,setB) :
    print("the difference to A-B is: ", setA.difference(setB))
    print(setA) 

def is_member_of_set(setB) :
    setC=set()
    setC.add(int(input("enter your number: ")))
    print("SetC is memeber of setB", setC in setB)
    
def set_display(setA):
	print(len(setA)) 
		
def set_add_element(setA):
    # setd=set()
    setA.add(int(input("enter your number: ")))
    print(setA)
    
def set_add_elements(setA):
    how_many_num=(int(input("enter how many num: ")))
    for i in range(0,how_many_num,1):
        setA.add(int(input("enter your numbers: ")))
    print(setA)

def set_remove_element(setA):
    remove=int(input("enter number you want to remove: "))
    setA.remove(remove)
    print(setA)
    
def my_set_store():
    print("\n Welcome to Our Set Store !!! ")
    
    setA=set()
    setB=set()
    
    how_many=(int(input("how many elements do you want: ")))
    for i in range(0,how_many,1):
        setA.add(int(input("enter your first  value: ")))
    print(setA)
    
    how_many=(int(input("how many elements do you want: ")))
    for i in range(0,how_many,1):
        setB.add(int(input("enter your second value: ")))
    print(setB)
    
    
    
    # input("Implement code to populate elements for SETA and SETB , assume they have integer value ")
    

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("	1: Union")
        print("	2: Intersection ")
        print("	3: A-B")
        print("	4: B-A")
        print("	5: Take a element from user and Display if that element is a member of set B ")
        print("	6: Display number of elements in the set A")
        print(" 7: Display number of elements in the set B")
        print("	8: Add an element taken from the user to the set A")
        print("	9: Add multiple elements taken from the user to the set A")
        print("	10: Remove an element taken from the user from set A")
        print(" 11: Exit")

        choice = int(input("Please enter your choice "))

        if choice   ==1:
            set_union(setA,setB) 
        elif choice ==2:
            set_intersection(setA,setB)
        elif choice ==3:
            set_minus(setA,setB)
        elif choice ==4:
            set_minus(setB,setA)
        elif choice ==5:
            is_member_of_set(setB) 
        elif choice ==6:
            set_display(setA)
        elif choice ==7:
            set_display(setB)
        elif choice ==8:
            set_add_element(setA)
        elif choice ==9:
            set_add_elements(setA)
        elif choice ==10:
            set_remove_element(setA)
        elif choice ==11:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")  
			
my_set_store()	