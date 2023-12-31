#reverse the text 
x=input("enter the string")
l=(x.split(' ')[::-1])
s=' '.join(l)
print(s)

#reverse the text in reverse order
x=input()
l=x.split(' ')
l2=l[::-1]
s=' '.join(l2)
print(s)

#to check for palindrome
x=input("enter the string=")
if x==x[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#to change to upper case
s=input("enter the string=")
print("uppercase",s.upper())
#to find the maximum length of the string
x=input("enter the string")
index=0
l=x.split(' ')
print(l)
length=max(len(e)for e  in l)
print(length)

#to find the string 

s=input()
maxlength=0
i=0
index=0
for w in s.split(' '):
    if maxlength<len(w):
        maxlength=len(w)
        index=i
    i+=1
print("maxlength word is",s.split(' ')[index])