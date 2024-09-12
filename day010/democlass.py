# class creation
# class my_student_info():
    
#     def __init__(self,rcv_name=None,rcv_rollno=None):
#         # instance variables
#         self.name = rcv_name
#         self.Rollno = rcv_rollno

#     # instance method
#     def get_student_details(self):
#         print(self.name,self.Rollno)

# # invocation by object creation 

# s1=my_student_info('gaurav',1)  
# s1.get_student_details()


# s2=my_student_info('sagar',2)
# s2.get_student_details()


# library management system
# attributes
# book_name and book_author and cost_price
# # methods
# display book name 
# display book author
# calculate the purchse price of lot of books where a lot(no of books is provided by the user)

# create one book and cost of purchase 10 books

class library_store():
    
    def __init__(self,rcv_book_name=None,rcv_book_Auth=None,rcv_cost_price = 1000):
        self.book_name=rcv_book_name
        self.book_Auth =rcv_book_Auth
        self.cost_price =int(rcv_cost_price)

def get_name_details(self):
        return self.book_name
        
def get_auth_name(self):
      return self.book_Auth       
    # def book_cost(self, cost_price):
    #     no_books = int(input("how many books"))
    #     cost_price = no_books * cost_price
    #     print("price of the books:", cost_price)
    #     print(book_cost(self, cost_price))
          
book=library_store('harry potter','jkrowling',(450 * int(input("how many books:"))))
book.get_library_details()
    

    
        
    
        
    

