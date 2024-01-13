#method overriding
class orders:
    def __init__(self):#here we define local variable with the self.
        self.cart=[] #instance variable
    def add_to_cart(self,items):
        self.cart.append(items)
    def remove_to_cart(self,items):
        self.cart.remove(items)
    def __len__(self): #this is instance method because it always access instance variable
        return len(self.cart)
    def __str__(self):
        items='cart contents:-'
        for i in self.cart:
            items+=i+' '
        return items
o=orders()
o.add_to_cart('colgate')
o.add_to_cart('paste')
o.add_to_cart('brush')
o.add_to_cart('biscuit')
o.add_to_cart('tofees')
o.remove_to_cart('tofees')
print(len(o))
print(o)