# 2. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 

class Person():
    
    def __init__(self,rcv_name=None,rcv_place_of_residence=None):
        self.name=rcv_name
        self.place_of_residence=rcv_place_of_residence
    
    def get_person_details(self):
        print(self.name,self.place_of_residence)
    
s1=Person('ojas','ratnagiri')
s1.get_person_details()


class Sister(Person):
    def __init__(self, rcv_name=None, rcv_place_of_residence=None,rcv_exam_subjects=[]):
        super().__init__(rcv_name, rcv_place_of_residence)
        self.exam_subjects=rcv_exam_subjects
    
        
    def get_exam_subjects(self):
        print(self.name,self.place_of_residence,self.exam_subjects)
        
s2=Sister('sakshi','pune',['English','maths'])
s2.get_exam_subjects()

    
class Uncle(Person):
    
    def __init__(self, rcv_name=None, rcv_place_of_residence=None,rcv_business=None):
        super().__init__(rcv_name, rcv_place_of_residence)
        self.business=rcv_business
    
    def display_busniess(self):
        print(self.name,self.place_of_residence,self.business)
        
s3=Uncle('venky','pashan','Python_programmer')
s3.display_busniess()
        
    
    
    
