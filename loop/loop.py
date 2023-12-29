#print the sum of n natural number
x=int(input("enter the number"))
s=0
for e in range(1,x+1):
    s=s+e
print("natural_sum",s)

x=int(input("enter the number"))
s=0
for e in range(1,x+1):
    s=s+e*e
print("square_sum",s)

x=int(input("enter the number"))
s=0
for e in range(1,x+1):
    s=s+e*e*e
print("cube_sum",s)

x=int(input("enter the number"))
for e in range(1,x+1):
    s=s+2*e+1
print("odd_sum=",s)

x=int(input("enter the number"))
for e in range(1,x+1):
    s=s+2*e
print("even_sum=",s)