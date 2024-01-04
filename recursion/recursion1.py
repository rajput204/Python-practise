def natural(n):
    if n==0:
        return 1
    else:
        natural(n-1)
        print(n,end=' ')
natural(10)
print( )

def reverse(n):
    if n==0:
        return 1
    else:
        print(n,end=' ')
        reverse(n-1)
reverse(10)
print( )
    
#print n odd natural number
def odd(n):
    if n==0:
        return 1
    else:
        odd(n-1)
        print(2*n+1,end=" ")
odd(10) 
print( )

#odd natural number in reverse order
def rodd(n):
    if n==0:
        return 1
    else:
        print(2*n+1,end=' ')
        rodd(n-1)
rodd(10) 
print( )

def printm(n):
    if n>0:
        print("mysirg")
        printm(n-1)
printm(5)