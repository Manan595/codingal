class vehile:
    def __init__(self,name,mileage,capicity):
        
        self.name=name
        self.mileage=mileage
        self.capicity=capicity


    def fare(self):
        return self.capicity*100
    


class Bus(vehile):
    def fare(self):
        amount= super().fare()
        amount += amount *10/100
        return amount
    
School_bus = Bus('school Volovo',12,50)
print('total Bus fare is :',School_bus.fare())