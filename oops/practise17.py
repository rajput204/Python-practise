#operator overloading
class rational:
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def __add__(self,other):
        p=self.p*other.q+self.q*other.p
        q=self.q*other.q
        sum=rational(p,q)
        return sum
    def __sub__(self,other):
        p=self.p*other.q-self.q*other.p
        q=self.q*other.q
        sub=rational(p,q)
        return sub
    def __str__(self):
        return str(self.p)+'/'+ str(self.q)
p=rational(2,3)
q=rational(1,3)
r=p+q
print(r)