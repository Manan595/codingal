class Cricle():
    def __init__(self,r):
        self.radius =r



    def area(self):
        return self.radius**2*3.14
    

    def perimeter(self):
        return 2*self.radius*3.14
    

radius = int(input("enter radius"))
Newcircle = Cricle(radius)
print(Newcircle.area())
print(Newcircle.perimeter())
