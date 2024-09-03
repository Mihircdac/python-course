name=input("Enter your Name: ")
salary= int(input("enter your salary: "))
incrementp=int(input("enter the increment percentage: "))

def inc_calc (name,salary,incrementp):
    finalincrement=salary+int((salary*incrementp/100))
    print("dear",name,"your salary is ",salary,"rs and you have an increment of ",incrementp,"percent so cograts you have your new salary as",finalincrement,"rs")
    
inc_calc(name,salary,incrementp)