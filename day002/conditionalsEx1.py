num=int(input("Enter Number: "))


if num % 3 == 0 and num% 5 == 0:
    print("FizzBuzz")
else:
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("Invild input")           
        
  
