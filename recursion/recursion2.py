#write a python program to print n even natural number
def neven(n):
    if n>0:
        neven(n-1)
        print(2*n,end=" ")
neven(10)
print( )

def reversen(n):
    if n>0:
       print(2*n,end=" ")
       reversen(n-1)
reversen(10)
print( )

def square(n):
    if n>0:
        square(n-1)
        print(n*n,end=" ")
square(10)
print( )

def cubes(n):
    if n>0:
        cubes(n-1)
        print(n*n*n,end=" ")
cubes(10)
print( )

#write a recursive funtion to print the reverse of a given number
def reverse(n):
    if n>0:
        print(n%10,end=' ')
        reverse(n//10) 
reverse(1234)