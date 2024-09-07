# Create a program named "my_dict_store" which support following operations on 
# dictionary named "capitals" which would have keys as their country and values as their capitals
# respectively from the user
# for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
# is provided by the user 

# Operations supported by our program are :
#     1: Display number of elements in the capitals collection
#     2: Add an element to the capitals collection like --> Afghanistan: Kabul
#     3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
#     4: Remove an element from the collection 	
#     5: Take a key from the user and show value if it is present in the dictionary
#     6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	


#Keep asking the user for the operation in this store untill he chooses to exit from the program

# Sample code template for my_dict_store
def dict_display_capitals(capitals): 
       print(capitals) 
     
def dict_add_element(capitals):
    Single_country=(input("enter your country name: "))
    single_capital=(input("enter the capital name: "))
    capitals[Single_country] = single_capital
    print(capitals)    
            
def dict_add_elements(capitals):
    num_of_countries=int(input("how many country you want? "))
    for i in range(0,num_of_countries,1):
        mycountry=(input("enter your country name: "))
        mycapital=(input("enter capital name: "))
        capitals.update({mycountry:mycapital})
    print(capitals)
        
            
def dict_remove_element(capitals):
    country_del =(input("which country to delete? "))
    del capitals[country_del]
    print(capitals)
    
    
        

def dict_show_value_for_a_key(capitals):
    key=input("enter your key: ")
    for key,values in capitals.items():
        print("the country is ",key,"and capital is ",values)
        
        
    
    
    
def dict_update_or_add_a_key(capitals):
    num_of_countries=int(input("how many country you want? "))
    for i in range(0,num_of_countries,1):
        mycountry=(input("enter your country name: "))
        mycapital=(input("enter capital name: "))
        capitals.update({mycountry:mycapital})
    print(capitals)
        
    

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
	
    capitals= {}
    no_of_countries=int(input("how many countries? "))
    for i in range(0,no_of_countries,1):
        country=(input("Enter your country name: "))
        capital=(input("Enter you country's capital: "))
        capitals[country]=capital
        
    print(capitals)
        
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Take a key from the user and show value if it is present in the dictionary")
        print("    6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	")
        print("    7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            dict_show_value_for_a_key(capitals)
        elif choice ==6:
            dict_update_or_add_a_key(capitals)
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()