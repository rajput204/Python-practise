#methodoverriding
class robot:
    def __init__(self,name):
        self.name=name #instance variable
    def say_hi(self):
        print("this is robot"+self.name)
class policerobot(robot):
    def say_hi(self):
         print("i am here to help u " +self.name)
p=policerobot("aditya")
p.say_hi()
