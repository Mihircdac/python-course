stock=input("enter your stock name: ")
buy=int(input("enter your buy price: "))
sell=int(input("enter your selling price: "))
units=int(input("enter no. of units bought: "))

profit=sell-buy
final_profit=(profit*units)
print("The profit made on ",stock,"by selling",units,"units of that stock is ",final_profit)

