#accessor and mutator

class customer:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def getname(self):
        print(self.name)
    def getphone(self):
        print(self.phone)
    def setphone(self,phone):
        self.phone=phone
    def showdetails(self):
        print(self.name)
        print(self.phone)
c=customer("aditya",987654332)
c.getphone()
c.setphone(8809493517)
c.showdetails()


