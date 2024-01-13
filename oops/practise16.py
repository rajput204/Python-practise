#method overriding
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c=circle(5)
print( c.area())
r=rectangle(5,12)
print(r.area())