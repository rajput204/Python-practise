class currency:
    def __init__(self,currency,rate):
        self.currency=currency
        self.rate=rate
    def get_currency(self):
        return self.currency
    def set_currency(self,currency):
        self.currency=currency
    def get_rate(self):
        return self.rate
    def set_rate(self,rate):
        self.rate=rate
    def convertor(self,amount):
        return self.currency +'conversion'+str( amount*self.rate)
c=currency('usd',70)
print(c.convertor(100))
c.set_currency('aud')
c.set_rate(50)
print(c.convertor(100))