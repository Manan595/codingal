class Ferrai:
    def fuel_type(self):
        print("pertrol")
    def max_speed(self):
        print("max speed is 380")

class BMW:
    def fuel_type(self):
        print('diesel')
    def max_speed(self):
        print('max speed is 240')

ferrai= Ferrai()
bmw= BMW()

for car in (ferrai, bmw):
    car.fuel_type()
    car.max_speed()