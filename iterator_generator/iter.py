# an iterator can  be +seen as a pointer to a container

#the iterator is a abstraction which enables the programmer's to access all the elements of the conatiner(a set,list and so on) without  qany deeper knowledge of the data structure of the container object.
#in  python  iterator is generated explicitly.

r=range(1,10,1)
it=iter(r) # can take any variable name rather than it
print(next(it))
print(next(it))
print(next(it)) #it will give the element as 1
 #it is an iterator for an particular iterable.

################ GEnerator
  

  #if the function of body contains yields then it is an generator

def f1():
    yield 10
    yield 20
    yield 30
g=f1()
for e in g: #it is generating function with the help of the function generator is always iterable
    print(e,end=" ")
print( )
# a=next(g) #generating the values from the function of code
# b=next(g) 
# c=next(g)
# print(a,b,c)

#writing a program to print n natural number using generator
def f1(n):
    i=1
    while i<=n:
        yield i #return through the next method
        i+=1
g=f1(10)
for e in g:
    print(e,end=" ")


#return ends the function execution
#yeild pause the function execution

#when ever u see the programming regarding to the patter then u can use the yield method here to find the gien solution of the problem.
#stopiteration is the error raised by the iterable.
l=[22,56,78,11,25]
it=iter(l)
while True: #infinite time true that's why it is true
    try:
       print(next(it),end=" ")
    except StopIteration:
        break
