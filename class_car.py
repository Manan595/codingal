class vehicle:
    def __init__(self, max_speed, mileage):

     self.max_speed=max_speed
     self.mileage=mileage

modelX= vehicle(240,18)


print("model Max speed:", modelX.max_speed)

print("model milage:", modelX.mileage)