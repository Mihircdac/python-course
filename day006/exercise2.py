def display_emp(employee_database):
    print(employee_database)
    
def display_id(employee_database):
    employee_database["employee_id"] = int(input("enter your id:" ))
    print(employee_database)
    
    
def display_name(employee_database):
    employee_database["employee_name"]=str(input("enter your name: "))
    print(employee_database)
    
def account_num(employee_database):
    employee_database["account_number"]=int(input("enter account number: "))
    print(employee_database)
    
def salary(employee_database):
    employee_database["salary"]=float((input("enter your salary in decimal form: ")))
    print(employee_database)
    
def address(employee_database):
    employee_database.update({"address": [str(input("home address: "))],"work_address": [str(input("work address: "))]})
    print(employee_database)
    
def awards(employee_database):
    awards_list = []
    num_awards = int(input("award list number:"))
    
    for i in range(0,num_awards,1):
        award = input("enter your award: ")
        awards_list.append(award)
    employee_database["awards"] = awards_list
    
    print(employee_database)
 
    
def subjects(employee_database):
    subject_list=[]
    num_of_subjects=int(input("enter how many subjects: "))
    
    for i in range(0,num_of_subjects,1):
        subject=[input("enter your subjects: ")]
        subject_list.extend(subject)
    employee_database["subjects_enrolled"]=tuple(subject_list)


    print(employee_database)

    
def emp_data():
    print("/welcome to the employee database system/")
    
employee_database={}
    
employee_database["employee_id"] = int(input("enter your id:" ))
employee_database["employee_name"]=str(input("enter your name: "))
employee_database["account_number"]=int(input("enter account number: "))
employee_database["salary"]=float((input("enter your salary in decimal form: ")))
# employee_database["home_address"]=[str(input("home address:" ))]
# employee_database["work_address"]=[str(input("work address:" ))]
employee_database.update({"address": [str(input("home address: "))],"work_address":[str(input("work address: "))]})
employee_database["awards"]=[(input("enter your awards: "))]
employee_database["subjects_enrolled"]=tuple([input("enter your subjects: ")])

print(employee_database)

while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all the employee record: ")
        print('    2: Display employee Id: ')
        print('    3: Display employee name: ')
        print("    4: show the account number: ")
        print("    5: show the salaries of the employee: ")
        print("    6: display home and work address: like home is here and work is there: ")
        print("    7: show awards given to the employee: ")
        print("    8: show the subjects enrolled: ")


        choice = int(input("Please enter your choice "))
        
       
        
        if choice   ==1:
            display_emp(employee_database) 
        elif choice ==2:
            display_id(employee_database)
        elif choice ==3:
            display_name(employee_database)
        elif choice ==4:
            account_num(employee_database) 
        elif choice ==5:
            salary(employee_database)
        elif choice ==6:
            address(employee_database)
        elif choice ==7:
            awards(employee_database)
        elif choice ==8:
            subjects(employee_database)
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

emp_data()


    

    
    
    
    
    
    

    




