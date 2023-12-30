from emoji import emojize
n=int(input("enter the range"))
l=[]
for e in range(1,n+1):
    if e%2==0:
        l.append(e)
print(l)
l=[45,89,78,55]
print(sum(l))

l=[int(e)for e in input().split(',')]
print(sum(l))

n=int(input("enter the range"))
a,b=0,1
l=[]
for e in range(0,n+1):
    
    c=a+b
    a=b
    b=c
    l.append(c)
print(l,end=" ")
print( )

#n term fibonacci series using for loop
n=int(input("enter the range"))
a,b=-1,1
l=[]
for e in range(1,n+1):
    c=a+b
    a=b
    b=c
    l.append(c)
print(l,end=" ")
print( )

#using while loop
n=int(input("enter the range"))
a,b=-1,1
l=[]
while n:
    c=a+b
    l.append(c)
    a=b
    b=c
    n-=1
print(l)

x=int(input("enter the number"))
l=[]
for e in range(1,x+1):
    for f in range(2,e):
        if e%f==0:
            break
    else:
        l.append(e)
print("prime number=",l)

#write  a python script to add two matrix of order 3*3 and store elements in a list of list


#write  python script to create two list from a given list of number in such a way that the first list can have only positive number and second list can have only non positive number.
print("enter the number seperated by comma")
x=input("enter the number")
l=[int(e)for e in x.split(',')]
l1=[]
l2=[]
for e in l:
    if e>0:
        l1.append(e)
    else:
        l2.append(e)
print("previous list=",l)
print("l1=",l1,end=" ")
print("l2=",l2)
print(emojize(":thumbs_up:")*10)
print("enter the first element row wise seperated by comma")
x=[[int(e)for e in input().split(',')],[int(e)for e in input().split(',')],[int(e)for e in input().split(',')]]
print("enter the second element row wise seperated by comma")
y=[[int(i)for i in input().split(',')],[int(i)for i in input().split(',')],[int(i)for i in input().split(',')]]
z=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
       z[i][j]= x[i][j]+y[i][j]
       print(z[i][j],end=" ")
    print( )
print( )

print("enter the first element row wise seperated by comma")
x=[[int(e)for e in input().split(',')],[int(e)for e in input().split(',')],[int(e)for e in input().split(',')]]
print("enter the second element row wise seperated by comma")
y=[[int(i)for i in input().split(',')],[int(i)for i in input().split(',')],[int(i)for i in input().split(',')]]
for i in range(0,3):
    for j in range(0,3):
       print( x[i][j]+y[i][j],end=" ")
       
    print( )

    
print( )
print(emojize(":smiley:")*10)
