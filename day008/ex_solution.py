class negative_number_error(Exception):
    pass

my_int_list1=[]
def create_positive_numbered_list(my_int_list1):
    for i in range(int(input("element count"))):
       value_entered = int(input("Element please"))
       if value_entered > 0:
        my_int_list1.append(value_entered)
       else:
           raise  negative_number_error
       print(my_int_list1)

create_positive_numbered_list(my_int_list1)

class positive_number_error(Exception):
    pass

my_int_list2=[]
def create_negative_numbered_list(my_int_list2):
    for i in range(int(input("element count"))):
       value_entered = int(input("Element please"))
       if value_entered < 0:
        my_int_list2.append(value_entered)
       else:
           raise  positive_number_error
       print(my_int_list2)
       
# create_negative_numbered_list(my_int_list2)       

def my_chosen_dataype_value():
    print("1:int")
    print("2:float")
    print("3:str")
    print("4:list")
    print("5:tuple")
    print("6:set")
    print("7:dict")

    choice = int(input("please choose"))
    if choice == 1:
        return int(input("enter the integer"))
    elif choice == 2:
        return float(input("enter the float"))
    elif choice == 3:                
        return input("enter the string")
    elif choice == 4:            
        temp_list = []
        for i in range(int(input("element_count"))):
            temp_value = my_chosen_dataype_value()
            temp_list.append(temp_value)
        return temp_list
    elif choice == 5:   
        temp_list = []
        for i in range(int(input("element_count"))):
            temp_value = my_chosen_dataype_value()
            temp_list.append(temp_value)
        return tuple(temp_list)
         
    elif choice == 6:
        temp_set = set()
        for i in range(int(input("element_count"))):
            while True:
                temp_val =  my_chosen_dataype_value()
                try:
                    flag = ''
                    temp_set.add(temp_val)
                    flag = 'added_to_set'
                except Exception:    
                    print("you chose a wrong dataype for the value of the set , please try again")
                if flag == 'added_to_set':
                    break
                    
        return temp_set    
        
    elif choice == 7:
        temp_dict = {}
        for i in range(int(input("element_count"))):
            temp_key = input("key")
            temp_val = my_chosen_dataype_value()
            temp_dict[temp_key]=temp_val
        return temp_dict    
    else:
        print("wrong_choice")    

# while True:
#     print(my_chosen_dataype_value())
#     ch=     input("N to exit")
#     if ch == 'N' or ch =='n':
#         break

class homogenous_list_error(Exception)     :
    pass

my_het_list3=[]
def create_list_and_check_if_heterogenous(my_het_list3):
        for i in range(int(input("element_count"))):
            temp_value = my_chosen_dataype_value()
            my_het_list3.append(temp_value)

        first_datatype_seen = type(my_het_list3[0])
        is_heterogenous = False
        for val in my_het_list3:
            if first_datatype_seen != type(val):
                is_heterogenous = True
                break
            
        if is_heterogenous == False:
            raise homogenous_list_error
        print("We have received a heterogenous list")        
            
create_list_and_check_if_heterogenous(my_het_list3)