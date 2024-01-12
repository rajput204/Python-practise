#inner class parmeter should be given to the constructor to make the inner class object
class computer:
    def __init__(self,name,make,os):
        self.name=name
        self.make=make
        self.cpu=self.cpu(make)
        self.os=self.os(os)
    def __str__(self):
        return self.name+self.make
    class cpu:
        def __init__(self,make):
            self.make=make
        def get_make(self):
            return self.make
    
    class os:
        def __init__(self,os):
            self.make=os
        def get_name(self):
            return self.name
c=computer("pc101",'intel','window')
print(c)
