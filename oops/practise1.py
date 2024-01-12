from random import*
class dice:
    def __init__(self,sides):
        self.sides=sides
    def rolldice(self):
        return randint(1,self.sides)
d=dice(12)
print(d.rolldice())
print(d.rolldice())