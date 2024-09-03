def fuel_cost(distance,mpg=50,fuel=1):
    return distance/mpg*fuel
    
       
distance=int(input("enter the distance: "))
print("the cost of travel in dollars is",fuel_cost(distance))

    