#higher order function takes function as an argument and returns a function
#we input function decorator # we have to write the decorator function just before the function definition  i.e something decoration type is applied on the result function
def deco_result(result_fun):
    def distinction(marks):
        for m in marks:
            if m>70:
                print(m,"distinction")  #here deco-result is the extra function 
        else:
            result_fun(marks)
    return distinction

@deco_result
def result(marks):
    for e in marks:
        if e>33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")

marks=[45,18,90,63,54]
result(marks) #when ever u call the result deco result will work.
print()

def deco_prime(prime_fun):
    def rprime(n):
        for i in range(2,n+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                 print(i,sep='-',)
        else:
            prime_fun(n)
    return rprime
@deco_prime
def prime(n):
        for j in range(2,n):
            if n%j==0:
                print(n,"not prime",sep='-')
                break
        else:
            print("prime")
prime(10)
print( )


#decorator function to check whether right angle or not right angle triangle
def deco_right_angle(right_angle):
    def right(a,b,c):
            if a**2==b**2+c**2:
             print("right angle")

            else:
               print(a,b,c,"not right angle triangle",end=" ")
            return right_angle
    return right

@deco_right_angle
def right_angle(a,b,c):
        if a**2==b**2+c**2:
           return True
        else:
            return False

right_angle(10,5,12)

print( )
print(chr(4)*20)



#define a decorator to display happy new year in the beginning
def d2(f1):#in f1 whole fun  function get passed as an argument.
    def greet():
        print("happy new year")
        f1()#due to call of f1 function hello get printed
    return greet
@d2#d2 function get activated and fun function get passed in f1 as an argument and it fill print the what d2 function is returning i.e greet
def fun():
    print("hello")
fun()

#working due to decorator the fun function pass as an argument in d1 and now greet function will come in an action

print(chr(4)*20)
#hcf

def d1(h1):
    def deco(a,b):
        x=h1(a,b)
        if (x==1):
            print("co-prime number's")
        else:
            print("not co-prime")
        return x
    return deco
@d1 #due to decorator d1 get activated  i.e hcf  6 and 8 get passed in deco as an argument
def hcf(a,b):
    h=a if a>b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1
    return h
print(hcf(6,8))
print( )
print(chr(4)*20)


#print good bye message at the end
def d2(f2):
    def greeting():
        f2()
        print("good bye")
    return greeting
@d2
def fun1():
    print("aditya")
fun1()


#output:-final output will be aditya good bye by changing the line in the beginning
#aditya
#goodbye