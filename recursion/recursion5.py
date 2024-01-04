#first natural number
def natural(n):
    if n==1:
        return 1
    s = n+natural(n-1)
    return s
print(natural(10))

#print n natural number in reverse order
def reverse(n):
    if n==1:
        return 1
    else:
        print(n,end=" ")
        return(reverse(n-1))
print(reverse(10))

#print n odd number
def odd(n):
    if n>0:
       odd(n-1)
       print(2*n+1,end=' ')
      
odd(5)
print( )


#print to print n  even number
def  even(n):
    if n>0:
        even(n-1)
        print(2*n,end=' ')
even(5) 
print( )

#n even natural number in reverse number
def re_even(n):
    if n>0:
        print(2*n,end= ' ')
        even(n-1)
re_even(5)
print( )


#sum of n natural number
def sum(n):
    if n==1:
        return 1
    else:
        s=n+sum(n-1)
        return s
print(sum(10))

#sum of first odd natural number
def sodd(n):
    if n==1:
        return 1
    else:
        s=(2*n+1)+sodd(n-1)
        return s
print(sodd(3))

# calculate the factorial of the number
def factorial(n):
    if n==1:
        return 1
    else:
        fact=n*factorial(n-1)
        return fact
print(factorial(5))

#sum of squares of n natural number
def s_square(n):
    if n==1:
        return 1
    else:
        s=n**2+s_square(n-1)
        return s
print(s_square(5))
#sum of first natural number
def square(n):
    if n==1:
        return 1
    s=n+square(n-1)
    return s
print(square(5))