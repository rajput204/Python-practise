# #to check the number is of three digit or not
# x=int(input("enter the number"))
# if x>99 and x<1000:
#     print("three digit number")
# else:
#     print("not three digit number")

# #to check the number is posititve negative or zero
# x=int(input("enter the number"))
# if x>0 :
#     print("positive")
# elif x<0:
#     print("negative")
# else:
#     print("zero")
# #to check the real and distinct root of the quadratic equation 
# a,b,c=int(input("enter the number")),int(input()),int(input())
# d=b**2-4*a*c
# if d>0:
#     print("print real and distinct root")
# else:
#     print("not real and distinct root")
    
#to find the greatest among the three number even if the number is same
n1,n2,n3=int(input()),int(input()),int(input())
if (n1>=n2) and (n1>=n3):
    print("greates is %d"%(n1))
elif(n2>=n1) and (n2>=n3):
    print("greates is %d"%(n2))
else:
    print("greatest is %d " %(n3))