#print the table of 5 
x=int(input("enter the time u want the multiple"))
for e in range(1,10+1):
    print("{}*{}={}".format(x,e,x*e))
print()
print("\u2764\ufe0f"*12)

#print the multiple of the 10
for e in range(1,10+1):
    print("{}*{}={}".format(10,e,10*e))
    print()
print("\u2764\ufe0f"*12)

#print m multiple of n
m=int(input("enter the  time multiple  u want "))
n=int(input("enter the number "))
for e in range(1,m+1):
    print("{}*{}={}".format(n,e,n*e))
print()
print("\u2764\ufe0f"*12)

#print 10 multiple in reverse order
n=int(input("enter the number"))
for i in reversed(range(9+1)):
    print("{}*{}={}".format(n,i,n*i))
print()

