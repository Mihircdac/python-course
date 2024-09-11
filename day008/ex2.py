# 4)Create the following program named "my_exception_store" with the menu below :

# Welcome User , What would you like to do today ?
#     1) Create a postive numbered list 
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     2) Create a negative  numbered list 
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
#     3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

#     4) Check if the element is present in the list 
#     Take the Input element that you would like to search
#     and which of the above three list that he want to search element from
#     Note : raise an exception if the element is not found in the list
#     with a message "Sorry, Element could not be found"
        
#     5) Refresh the program to start with blank lists
#     6) Exit

# Handle exceptions in the script for all operations 
# and let the user continue till he chooses to exit from the program 

# reference code :

class negative_number_error(Exception):
    pass
def check_positive(my_int_list1):
    how_many_num = int(input("How many numbers?: "))
    for i in range(0,how_many_num,1):
            value = int(input("Enter number: "))
    try:
            if value > 0:
                my_int_list1.append(value)
            else:
                raise negative_number_error
    except  negative_number_error:   
            print("the number you have entered are negative: not valid") 
    

    
class positive_number_error(Exception):
    pass
def check_negative(my_int_list2):
    how_many_num = int(input("How many numbers?: "))
    for i in range(0,how_many_num,1):
            value = int(input("Enter number: "))
    try:
            if value < 0:
                my_int_list2.append(value)
            else:
                raise positive_number_error
    except  positive_number_error:   
            print("the number you have entered are positive: Not Valid")



def choice(my_het_list3):
    print("enter 1 for int: ")
    print("enter 2 for str: ")
    num=int(input("enter your int num: "))
    if num ==1:
        value1=int(input("enter you num: "))
        print("your input int are: ",value1 )
    elif num ==2:
        value2=str(input("enter your str: "))
        print("your str is : ",value2)
        break
    else:
        print("invalid boi:)")
 
 
            

class same_datatype(Exception):
    pass
def check_hetro((my_het_list3):
    how_many_num=int(input("enter your input quantity: "))
    for i in range(how_many_num):
        
        for i in range(0,my_het_list3):
            value=int(input("enter numbers: "))
    try:
        if value is :
            my_het_list3.append(value)
        else:
            raise same_datatype
    except same_datatype:
        print("not of the same datatype: invalid boi")
        
class homogeneous_list_error(my_het_list3):
    num=int(input("enter num you wanna add to the list: "))
    for i in range(1,num+1):
        choice(my_het_list3)
    for i in range(o,len(my_het_list3)):
        type1=type(my_het_list3[0])
        try: 
            if type1==type(my_het_list3[i]):
                continue
            else:
                raise homogeneous_list_error
        except homogenous_list_error:
        print("homogenous list encountered")
    



    
    
    
    
    


def my_exception_store(): 
    
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) hetro  ")
            print("4) Check if the element is present in the list ")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                check_positive(my_int_list1)
            elif choice ==2:
                check_negative(my_int_list2)
            elif choice ==3:
                check_hetro(my_het_list3)
            elif choice ==4:
                print("Lists created are as below \n ----------------------")
                print(f"1 : {my_int_list1}")
                print(f"2 : {my_int_list2}")
                print(f"3 : {my_het_list3}")
                
                while True:
                    check =int(input("Which of the below list you would want to search from "))
                    
                    if  check == 1:
                        find_an_element(my_int_list1)
                        break
                    elif check == 2:
                        find_an_element(my_int_list2)
                        break
                    elif check ==3:
                        find_an_element(my_het_list3)    
                        break
                    else:
                        print("Please choose something from the above")
            elif choice ==5:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==6:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except : same_datatype   
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
            
my_exception_store()   