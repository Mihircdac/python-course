class employee():
    
    #class variable 
    department_name="science"
    
    
    @classmethod
    def get_department_name(cls):
        return cls.department_name
    
    
    def __init__(self,rcv_emp_id=None,rcv_emp_salary=None,rcv_mgr_id=None):
        self.emp_id=rcv_emp_id
        self.__emp_salary=rcv_emp_salary
        self.mgr_id=rcv_mgr_id
        
    def get_emp_id(self):
         return self.emp_id   
        
    def get_emp_salary(self):
        return self.__emp_salary
    
    def get_mgr_id(self):
        return self.mgr_id
    
    def set_emp_salary(rcv_emp_salary):
        return rcv_emp_salary.__emp_salary
        

s1=employee(100,1000,1)
print("employee id is: ",s1.get_emp_id(), "salary:",s1.get_emp_salary(),"the mgr id is : ", s1.get_mgr_id())

new_salary=int(input("enter new salary"))    
s2=employee(100,new_salary,11) 
print("the set emp salary is: ",s2.set_emp_salary())         