#higher-function are those function which takes function as an argument
#the higher-order function are the map(),filter(),reduce()

#map in the map function
#map(function,iterables)
def square(a):
    return a*a
x=map(square,[1,2,3,4])
print(x)
for e in x:
    print(e,end=" ")
l=list(x)
print( )

#filter function is used for filtering the data from the data values
#filter(function,iterable)
def f(a):
    if a<4:
        return a
y=filter(f,(1,2,3,4)) #u can pass map,lambda inside the filter because it is also filter too
print(y)
l=[]
for e in y:
    l.append(e)
print(l)

#reduce function help to reduce the function and return in the single value
#we have to import it from using the functool
from functools import reduce
x=reduce(lambda a,b:a+b,[1,2,3,4])
print(x)
#two distinct method of finding the lambda function
from functools import reduce
def r(a,b):
    return a+b
x=reduce(r,[1,2,3,4])
print(x)


#assignment based on the map,filter reduce.


#1.
#2.
def vowel(a):
    count=0
    for e in a:
        if e in "aeiouAEIOU":
            count+=1
    return count
x=map(vowel,["gopal","jaipur","kanpur","patna"])
d={}
for e in x:
    print(e)
print( )


def digitcount(n):
    count=0
    while n:
        n=n//10
        count+=1
    return count
x=map(digitcount,(123,456,89741))
for e in x:
    print(e,end=" ")