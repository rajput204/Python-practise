try:
    a=int(input("enter first number"))
    b=int(input("enetr the second number"))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else: # it will work when ever there is no  error created by the  try block
    print("no error found")
finally:
    print("i am executed")