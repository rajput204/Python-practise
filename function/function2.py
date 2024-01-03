#program to make a fnction that's takes something and return something
def sum(a,b):
    return(a+b)
x=sum(10,20)
print(x)
print( )
#are of circle
def a_circle(r):
    return 3.14*r**2
y=a_circle(10)
print(y)
print( )

#average of three number
def average(a,b,c):
    return((a+b+b)/3)
z=average(10,20,30)
print(z)
print( )


#volume of cuboid
def volume(l,b,h):
    return l*b*h
l=volume(4,5,6)
print(l)
print( )
#
def compound(p,r,t):
    amount=p*(1+r/100)**t
    return amount-p
m=compound(1000,2,2)
print(m)
print( )
