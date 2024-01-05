x=(lambda a:True if a%2==0 else False)(10)
print(x)

x=(lambda r:3.14*r*r)(10)
print(x)

f=(lambda n: n if n==0 or n==1 else f(n-1)+f(n-2))
print(f(10))

hcf=lambda a,b: (b if a%b==0 else hcf(a%b,b)) if a>b else(a if b%a==0 else hcf(a,b%a))
print(hcf(12,18))

x=lambda text:len(text.split(' '))
t=("aditya a good guy")
print(x(t))