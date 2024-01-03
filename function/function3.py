#write a python function to check the even or odd number

def even_odd(n):
    return n%2==0
x=even_odd(10)
print(x)
print( )


#greatest among three number
def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
           return c
    else:
        if b>c:
            return b
        else:
            return c
y=greatest(10,20,1)
print(y)
print( )

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
           return False
    return True
is_prime(9)
print( )

def leap(y):
    if y%400==0:
        return True
    elif y%100==0:
       return True
    elif y%4==0:
       return True
    else:
        return False
Y=int(input("enter the year"))
print(leap(y))

#factorial of the number
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input())
print(fact(n))

def factorial(n):
    i=1
    while n:
        i=i*n
        n-=1
    return i
x=factorial(5)
print(x)
    

        
          
