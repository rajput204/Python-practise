class angle:
    def __init__(self,angle):
        self.angle=angle
    def __add__(self,other): 
        new_angle=angle(self.angle+other.angle)#parameter will take self ka angle and other ka angle
        return new_angle
    def __str__(self):
        return "degree"+str(self.angle)
a=angle(30)
a2=angle(60)
print(a+a2)
print()