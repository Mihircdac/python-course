'''
Write Python code that asks the user for a number in the range of 1 through 7. Display the corresponding day of the week where 
1 for Monday
2 for Tuesday 
3 for Wednesday 
4 for Thursday
5 for Friday
6 for Saturday
7 for Sunday. 
If the user enters a number outside the range of 1 - 7, print “error, out of range”.
'''

num=int(input("enter a number between 1 to 7: "))

if num==1:
    print("Monday")
    
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("error, out of range")
print("This is your day")
    
