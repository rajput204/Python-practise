
# #find the count of the given number
# x=input("enter the number")
# count=0
# for e in x:
#     count+=1
# print(count)
# #find the factorial of the number
# x=int(input())
# fact=1
# while x:
#    fact=fact*x
#    x-=1
# print(fact)

#sum of the digit 

#to print the binary equivalent of the number
#the octal equivalent of the number

d=24
s=''
while d!=0:
    s=str(d%2)+s #remainder would be 0
    d=d//2 #d would be 12 now d value will be 12
    print("binary=",s)

#to print the octal
    d=24
    s=""
    while d!=0:
        s=str(d%8)+s
        d=d//8
        print("octal conversion=",s)



