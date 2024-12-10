def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "charlotte" == city:
     return 183

    elif 'Tampa'== city :
       return 220
    elif 'pittsburgh' == city:
       return 222
    elif' Los angles' == city:
       return 447
    
    def rental_car_cost(days):
       if days>=7:
          return 40*days -50
       elif days>=3 :
          return 40*days -20
       else:
          return 40*days
def trip_cost(city, days, spending_money):
   return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("cost of rental car",rental_car_cost(5))

print("cost of a planet ride", plane_ride_cost("Los angles "))

print("cost of a hotel room")

print("The total cost of the trip", trip_cost("Los angles",7,500))

print(trip_cost("Tampa",6,500))