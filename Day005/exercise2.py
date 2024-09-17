# Sample code template for my string store starts
def string_display(string_input) :
    print(string_input) 

def display_3_4_5_element(string_input) :
    print(string_input[2:5]) 

def string_retrieve_element(string_input):
    print(string_input[1]) 

def string_retrieve_elements(string_input) :
    print(string_input[1:3]) 

def find_min_element(string_input) :
    print("the min num is: ",min(string_input)) 

def reverse_string(string_input) :
    string_input=tuple(reversed(string_input)) 
    print(string_input)

def  find_each_character_count(string_input):
    list=[]
    for i in string_input:
        cnt=string_input.count(i)
        list.append(tuple([i,cnt]))
    print(list)

def  find_character_count_greater_than_1(string_input):
    list=[]
    for i in string_input:
        cnt = string_input.count(i)
        if cnt > 1:
            list.append(i)
        else:
            print("None")
            
    print(list)       
            
def  check_palindrome(string_input):
    
        # strings=tuple(reversed(string_input))
        # print(strings)
    # string_input = string_input[: : -1]
    #  print(string_input)
    
    
    # strings=tuple(reversed(string_input))
    # print(strings)
    
    # if strings==string_input:
    #     print("is a palindrome")
    # else:
    #     print("not a palindrome")
    
    is_palindrome = True
    str_1 = string_input[: : -1]
    for i in (0 , string_input,1 ):
        for j in (0 , str_1,1):
          if string_input[i] == string_input[j]:
              continue
        else: 
            
            break
          
                  
pass

i = 0
j = -1   
  
if string_input(i) == string_input(j):
            i += 1
            j -= 1
            print("palindrome")
else:
        print("is not")
 
      
def my_string_store():
    print("\n Welcome to Our string Store !!! ")
    string_input = input("Please enter a string that you would want to perform Operation Upon:  ").strip()
    
    # hoW_many_string = int(input("string numbers:" ))
    # for i in range(0, hoW_many_string, 1):
    #     string_input = (input("Enter string:"))
        
    # print(string_input)
        

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display the string")
        print("  2:  Display third, fourth and fifth element from the string ")
        print("  3:  Retrieve element at a given subscript")
        print("  4:  Retrieve elements from a given subscript and to a given subscript")
        print( " 5:	 Find minimum character in the string " )
        print( " 6:	 Reverse the string " )
        print( " 7:	 Output list of tuple( character,count) for each characters of the string  " )
        print( " 8:	 Output list of characters of the string that appear more than once " )
        print( " 9:  Check if the string is a palindrome and return output message accordingly")
        print("  10: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            string_display(string_input) 
        elif choice ==2:
            display_3_4_5_element(string_input) 
        elif choice ==3:
            string_retrieve_element(string_input)
        elif choice ==4:
            string_retrieve_elements(string_input) 
        elif choice ==5:
            find_min_element(string_input) 
        elif choice ==6:
            reverse_string(string_input) 
        elif choice ==7:
             find_each_character_count(string_input)
        elif choice ==8:
             find_character_count_greater_than_1(string_input)
        elif choice ==9:
             check_palindrome(string_input)
        elif choice ==10:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_string_store()
# Sample code template for my string store ends