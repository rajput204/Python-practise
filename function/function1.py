#taking nothing and returning nothing

def add():
    a=int(input())
    b=int(input())
    c=a+b
    print("sum",c)
add()

#taking something returning nothing
def add(a,b):
    c=a+b
    print(c)
add(10,20)

#takes nothing and return something
def add():
    a=int(input())
    b=int(input())
    c=a+b
    return c
s=add()
print(s)
#takes something and return something
def add(a,b):
    c=a+b
    return c
add(500,20)