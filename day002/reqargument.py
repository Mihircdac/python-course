source=input("enter your source: ")
dest=input("enter your destination: ")
fare=int(input("enter your fare: "))
discount=int(input("enter the discounted price: "))

def fare_details(source,dest,fare=1000,discount=5):
    rate= fare/100*discount
    finaldes=int(fare-rate)
    print("fare from ", source,"to",dest,"is ",fare,"INR after applied discount of ",discount,"percent is ",finaldes)
    
fare_details(source,dest,fare,discount)
fare_details(source,dest)