class My_student_info():
    def __init__(self,rcv_name=None,rcv_rollno=None):
        # instance variables
        self.name = rcv_name
        self.Rollno = rcv_rollno
        
        

    # instance method
    def get_student_details(self):
        print(self.name,self.Rollno)

s1=  My_student_info('gaurav',1)     
s1.get_student_details()

class My_duasp_student_info(My_student_info):
    
    def __init__(self, rcv_name=None, rcv_rollno=None,rcv_hobbies=[],rcv_stipend=100,rcv_powers=[]):
        super().__init__(rcv_name, rcv_rollno)
        self.hobbies = rcv_hobbies # additional
        self.stipend = rcv_stipend # additional
        self.powers=rcv_powers

    # instance method # modified # oveririding
    def get_student_details(self):
        print(self.name,self.Rollno,self.hobbies,self.stipend,self.powers)
        
    # instance method # added
    def add_hobby(self,rcv_hobby):
        self.hobbies.append(rcv_hobby)
        
    def add_powers(self,rcv_powers):
        self.powers.append(rcv_powers)
        
    # # instance method # overloading not supported
    # def get_student_details(self,salutation):
    #     print(salutation+' '+self.name,self.Rollno,self.hobbies,self.stipend)
    
        

duasp_stud=My_duasp_student_info('adarsh',2,['painting',input("enter power:")])
# d uasp_stud.get_student_details("power: ", duasp_stud.add_powers())
# duasp_stud.get_student_details('mr')
print("Power:", duasp_stud.add_powers())