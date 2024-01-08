"""method overriding"""
from math import *
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):   #this is the method that we are overriding
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return pi*(self.radius*self.radius)
r=rectangle(10,5)
print(r.area())