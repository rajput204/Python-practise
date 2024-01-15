#write a generator to produce first N prime number
def prime(n):
    for e in range(1,n+1):
        for j in range(2,e):
            if e%j==0:
                break
        else:
            yield(e)
g=prime(10)
for e in g:
    print(e,end=" ")
print( )

#n term fibonacci series

def f2(n):
    a=-1
    b=1
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        yield(c)
g=f2(10)
for e in g:
    print(e,end=" ")
print( )

#square of n natural number
def natural(n):
    i=1
    while i<=n:
        yield(i*i)
        i+=1
g=natural(10)
for e in g:
    print(e,end=" ")
print( )

#use iter and next method to print values of a given list using while loop which works equivalent to for loop
l=[56,89,23,10,45,77,6,9]
it=iter(l)
while True:
    try:
        print(next(it),end=" ")
    except StopIteration:
        break
print( )

#user iter and next method to check if all the elements of list are even number using while loo which should be equivalent to for loop
#best question based on the iter function
def if_all(l,iseven):
    it=iter(l)
    while True:
        try:
            if not iseven(next(it)):
                return False
        except StopIteration:
            break
    return True #all numbers are even after execution of the while loop .
print(if_all([2,4,6,8,10,12,14],lambda n:n%2==0))
print( chr(4)*20)
print( )