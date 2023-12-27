#printing the name five time
x="aditya"
i=1
while(i<=5):
    print(x)
    i+=1

#print 10 natural number
i=1
while(i<=10):
    print(i)
    i+=1
print()

#reverse order printing of the 10 natural number
    
i=10
while(i>=1):
    print(i)
    i-=1
print()

#print first 10 odd natural number
i=1
while(i<=10):
    print("odd number=",2*i+1)
    i+=1
print()
#odd natural number in reverse order
i=10
print("reversed odd number")
while(i>1):
    print(2*i+1)
    i-=1
print()

#print first even natural number
i=1
while(i<=10):
    print(2*i,end=' ')
    i+=1
print()
#even natural number in reverse order
print("reversed even number")
i=10
while(i>1):
    print(2*i,end=' ')
    i-=1
print()
#even 10 even natural number 
print("square of the natural number ")
i=1
while(i<=10):
    print(i*i,end=' ')
    i+=1
print()

print("cubes of the natural number")
i=1
while(i<=10):
    print(i*i*i,end=' ')
    i+=1
print( )

#print the table of the 5
print("table of 5")
i=1
while(i<=10):
    print("{}*{}={}".format(5,i,5*i))
    i+=1
