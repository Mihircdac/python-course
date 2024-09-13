# # class airline():

# # li = set("2354", " 1556", "1562")
# # how_many_times = int(input("Enter number:"))
# # # s = set( "13")
# # d = {}
# # for i in range(0, how_many_times, 1):
# #     start_place = input("Enter start destination:")
# #     arrival_place = input("arival Destination :")
# #     d[start_place] = arrival_place
# #     if d == " " :
# #             d.add(li[i])
# #     else:
# #         print("invalid stat and end destinatio")
# # print(d)


# class Airline_ticket():
#     s = set()
#     d = {}
    
   
        
#     def __init__(self,rce_start_place = None , rcv_Arrival_place = None): 
#             self.start_place= rce_start_place
#             self.Arrival_place = rcv_Arrival_place
            
#     def gets_start_Destination(self):
#         input("Enter start")
#             # how_many_times = int(input("Enter number:"))
#             # for i in range(0 , how_many_times , 1):
#             #     start_Place = input("Enter Start Destination")
#             #     Arrival_place = input("Enter end destination:")
#             #     d[start_Place] = Arrival_place  
#         return self.start_place
        
#     def get_end_Destination(self):
#         input("Enter end")
#         return self.Arrival_place
    
# s1=Airline_ticket()
# print("Enter start", s1.gets_start_Destination(), s1.get_end_Destination())



class My_airline :
    airline_name = 'Gaurav Airline'
    cities = {'Delhi','Pune','Mumbai','Bangalore','Chennai','Hyderabad','Patna','Trivandrum'}
    rows = set(range(1,21))
    section = {'A','B','C','D','E','F'}
    flight_numbers = set(range(564262,564270))
    
    def __init__(self,rcv_dep = None , rcv_arr= None):
        
        if rcv_dep is None: 
            self.departure =  My_airline.cities.pop()
        else: 
            self.departure =  rcv_dep
            
        if rcv_arr is None:
            self.arrival = My_airline.cities.pop()  
        else:
            self.arrival =rcv_arr
            
        self.flight_number =  My_airline.flight_numbers.pop()  
        self.seat_number = str(My_airline.rows.pop()) + My_airline.section.pop() 
        
    def display_details(self):
        print(f"""Your ticket details :
--------------------------------------               
Airline_name : {My_airline.airline_name}
Flight_number : {self.flight_number}
Departure: {self.departure}
Arrival: {self.arrival}
Seat_number: {self.seat_number}
              
              """)   


def main():
   ticket_number1 = My_airline('LONDON','USA') 
   ticket_number2 = My_airline()
   ticket_number3 = My_airline(input("departure"),input("arrival")) 
   
   ticket_number1.display_details()
   ticket_number2.display_details()
   ticket_number3.display_details()

main()