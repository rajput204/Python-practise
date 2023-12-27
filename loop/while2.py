#to print first n even natural number

x=int(input("the number u want to enter the digit"))
i=1
while i<=x:
    print(2*i,end=" ")
    i+=1
print()

#to print n even natural number in reverse order
print("rervsed even number")
x=int(input("enter the number"))
while x:
    print(2*x,end=" ")
    x-=1
print()

#to print the square of first natural number
x=int(input("enter the number:"))
i=1
while i<=x:
    print(i*i,end=" ")
    i+=1
print()
print(chr(4)*10)
print("the cubes of the inputted number")
x=int(input("the inputted number"))
i=1
while i<=x:
    print(i*i*i,end=" ")
    i+=1
print( )


x=int(input("the inputted number"))
i=1
while i<=10:
    print("{}*{}={}".format(x,i,x*i))
    i+=1