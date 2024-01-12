#static method
class calculator:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a//b
    @staticmethod
    def mdiv(a,b):
        return a%b
print(calculator.add(10,2))
print(calculator.mul(10,2))
print(calculator.mdiv(10,2))
print(calculator.div(10,2))