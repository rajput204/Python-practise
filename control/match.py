x=int(input("enter a number"))
match x:
    case x if x>99 and x<1000:
        print("three digit")
    case __:
        print("not three digit number")
#to checck the positive or negative number
x=int(input("enter the the number"))
match x:
    case x if x>0:
        print( "positive number=%d"%(x))
    case x if x<0:
        print("negative number=%d"%(x))
    case __:
        print("zero")
print()
print(chr(6)*10)
#menu driven programm
print("1.odd-even")
print("2.positive-non_positive")
print("3.simple_interest")
print("4.quadratic_equation")
x=int(input("enter the desired number"))
match x:
    case 1:
        x=int(input())
        print("even") if x%2==0 else print("odd")
    case 2:
        x=int(input("enter the number"))
        print("positive") if x>0 else print("negative")
    case 3:
        p,r,t=int(input("principal")),int(input("rate")),int(input("time"))
        print("simple interest="%(p*r*t)/100)
    case 4:
        a,b,c=int(input()),int(input()),int(input())
        d=b**2-4*a*c
        print("real root" if d>0 else "distinct root")
    case __:
        print("select the default option")
#

