#inheritance
import math
class polygon:
    def __init__(self,ns,*sides):
        self.ns=ns
        self.sides=sides
class triangle(polygon):
    def __init__(self,ns,*sides):
        self.sides=sides
        super().__init__(ns,*sides)
    def area(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
t=triangle(3,10,15,9)#first one will take number of sides and another  one will take tuples of sides
print('area =',t.area())
print(type(t))