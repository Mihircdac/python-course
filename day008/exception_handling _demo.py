# basic understanding
# try:
#     age = int(input("enter age"))
# except Exception:
#     age = int(input("enter age again you entered a string value "))
# finally:
#     print("I am executed no matter what")        

# if age>18:
#     print("This person is eligible for voting")
    
# #

# having single exception ( parent)
# try:
#     documents = []
#     for i in range(2):
#         documents.append(input("enter valid documents"))

#     print("Document 1 was",documents[0]) 
#     print("Document 2 was",documents[1]) 
#     print("Document 2 was",documents[2]) 
    
# except Exception as e :
#     print("exception encountered",e.with_traceback(None))

# having mu;ltiple exceptions and its propogation
# try:
#     documents = []
#     for i in range(3):
#         documents.append(input("enter valid documents"))

#     print("Document 1 was",documents[0]) 
#     print("Document 2 was",documents[1]) 
#     print("Document 2 was",documents[2]) 
#     t= 90/0
# except IndexError as e:    
#      print("Index error encountered",e.with_traceback(None))  
# except Exception as e:    
#      print("exception encountered",e.with_traceback(None))       


# exception propogation
# def f1():
#     t= 90/0
         
# def f():
#     documents = []
#     for i in range(2):
#         documents.append(input("enter valid documents"))

#     print("Document 1 was",documents[0]) 
#     print("Document 2 was",documents[1]) 
#     # print("Document 2 was",documents[2]) 
#     f1()
# try:
#     f()
# except IndexError as e:    
#      print("Index error encountered",e.with_traceback(None))  
# except Exception as e:    
#      print("exception encountered",e.with_traceback(None))  


# custom exception / user defined exceptions

# class my_custom_exception(Exception):
#     pass 

# try:
#     age = int(input("enter age"))
# except Exception:
#     age = int(input("enter age again you entered a string value "))

# try:        
#     if age<18:
#         raise my_custom_exception
# except my_custom_exception:    
#         print("you entered an age less than 18")    
#         raise    
   
# print("This person is eligible for voting")        
        

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")