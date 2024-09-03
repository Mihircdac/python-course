def stock_price(stock,buy,sell,units,salary):
    profit=sell-buy
    final_profit=(profit*units)
    fsalary =final_profit+salary
    print("The profit made on ",stock,"by selling",units,"units of that stock is ",final_profit,". your salary will become",fsalary)

stock=input("enter your stock name: ")
buy=int(input("enter your buy price: "))
sell=int(input("enter your selling price: "))
units=int(input("enter no. of units bought: "))
salary=int(input("enter your salary: "))

stock_price(stock,buy,sell,units,salary)