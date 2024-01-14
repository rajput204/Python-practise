#user defined exception case
try:
    a=int(input("enter the number"))
    b=int(input("eneter the number"))
    if b==0:
      raise ZeroDivisionError("cannot divided by zero")
    c=a/b
    print(c)
except ZeroDivisionError as e:
   print(e)
print("program still continues")
print( )