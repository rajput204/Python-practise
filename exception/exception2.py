try:
    a=int(input("enter the number"))
    b=int(input("enetr the second number"))
    c=a/b
    print(c)
except(ZeroDivisionError):
    print("zerodivisionerror" ) 
except TypeError:
    print("inputted wrong datatype")
except ValueError:
    print("valueerror")
else:
    print("nothing error is found")
finally:
    print("code gets executed automatically")