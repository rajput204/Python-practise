#polymorphism
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name)
        print(self.age)
    def make_sound(self):
        print("meow-meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('name',self.name)
        print('age',self.age)
    def make_sound(self):
        print("bahu-bhau")
def pet(animal):
    animal.make_sound()
c=cat('kitty',2)
c.make_sound()
print(chr(4)*20)
d=dog("puppy",5)
d.make_sound()
print(d.info())