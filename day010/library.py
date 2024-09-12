class Library_management():
    
 #class variable
    library_name="Pune library"
    __library_turnover=1000
    
    @classmethod
    def get_library_name(cls): 
        return cls.library_name
        
    @classmethod
    def get_turnover(cls):
        return cls.__library_turnover
    
    # def cost_turnover(self):
    #     return self.__library_turnover
    
    #instance Variable
    def __init__(self,rcv_book_name=None,rcv_book_author=None,rcv_cost_price=None):
                 self.name=rcv_book_name
                 self.__price = rcv_cost_price
                 
    
    #instance method 
    def get_book_name(self):
        return self.name
    
    def get_cost_price(self):
        return self.__price
    
    
s1=Library_management("potter", "abc",200)   
print("name for s1", s1.get_book_name(), s1.get_cost_price() ) 

s2=Library_management()
print("library name", s2.get_library_name(), "turnover", s2.get_turnover())
            

    
    
    