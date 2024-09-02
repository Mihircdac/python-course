source=input("enter your source: ")
dest=input("enter your destination: ")
fare=int(input("enter your fare: "))
discount=int(input("enter the discounted price: "))

rate= fare/100*discount
finaldes=fare-rate
print("fare from ", source,"to",dest,"is ",fare,"INR after applied discount of ",discount,"percent is ",finaldes)