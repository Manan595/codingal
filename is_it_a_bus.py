class vehile:
    
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage


class Bus (vehile):
    pass


School_Bus= Bus('school Volovo',180,12)
print('vehile',School_Bus.name,'speed',School_Bus.max_speed,'mileage',School_Bus.mileage)