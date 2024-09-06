# Sample code template for My tuple store starts
def tuple_display_members(members) :
	print(members)

def display_3_4_5_element(members) :
	print(members[2:5])

def tuple_retrieve_element(members):
	print(members[1])

def tuple_retrieve_elements(members) :
	print(members[1:4])

def find_min_element(members) :
	print("Minimum element:", min(members))

def reverse_tuple(members):
    members = tuple(reversed(members))
    print(members)

			
def my_tuple_store():
    print("\n Welcome to Our tuple Store !!! ")
    print("Please enter a tuple Comma seperated that you would want to perform Operation Upon")
    
    # Write code to populate the members collection with list of names
how_many_people =int(input("Enter members: "))
members =[]
for i in range(0 , how_many_people, 1):
        members.append(input("member"))
        
members =tuple(members)
        
    
print("populate members here at this point and it should be tuple")

while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display all elements of the tuple")
        print("  2:  Display third, fourth and fifth element from the collection ")
        print("  3:  Retrieve element at a given subscript")
        print("  4:  Retrieve elements from a given subscript and to a given subscript")
        print( " 5:	 Find minimum element in the tuple " )
        print( " 6:	 Reverse elements in the tuple " )
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            tuple_display_members(members) 
        elif choice ==2:
            display_3_4_5_element(members) 
        elif choice ==3:
            tuple_retrieve_element(members)
        elif choice ==4:
            tuple_retrieve_elements(members) 
        elif choice ==5:
            find_min_element(members) 
        elif choice ==6:
            reverse_tuple(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")
            

my_tuple_store()		
# Sample code template for My tuple store ends