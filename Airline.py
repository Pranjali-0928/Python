import random
import string
class Airline:
    
    def __init__(self,departure,arrival_cities):
        self.departure = departure
        self.arrival = arrival_cities
        
        
       
    # def generate_seat_number(idx, num):
    #           return "M{}-{}".format(idx, i)
        randomLetter = random.choice(string.ascii_letters)
        y = random.randrange(1,21)
        seat_assigment1=(str(y)+randomLetter)  
        flight_number = set(range(564262,564362)).pop()
        print(f"departure from : {departure}\n arrival at : {arrival_cities}\n flight number is : {flight_number}\n seat number is : {seat_assigment1}")
def main():
       
      depar=input("enter departure name")
      arrival_city=input("enter arrival city")
      
    #   seat_assigment1 =list(map(lambda i: f'M1-{i}', range(1, 11)))
      ticket= Airline(depar,arrival_city)
      
if __name__=="__main__":
    main()