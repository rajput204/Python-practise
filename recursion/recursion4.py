def sum(n):
    if n==0:
      return 0
    else:
      return sum(n//10)+n%10
print(sum(123))

def factorial(n):
    if n==1:
      return 1
    else:
       return n*factorial(n-1)
print(factorial(5))

def binary(x):
   if x>0:
      binary(x//2)
      print(x%2,end=" ")
binary(25)
print( )

def octal(x):
   if x>0:
      octal(x//8)
      print(x%8,end=' ')
octal(25)
print( )

