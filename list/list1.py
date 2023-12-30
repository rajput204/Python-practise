print("enter the number seperated by comma")
n=input()
print(n)
l=[int(e)for e in n.split(',')]
print("sum=",sum(l))

print("enter the number seperated by comma")
n=input()
print(n)
l=[int(e)for e in n.split(',')]
print("avg=",sum(l)/len(l))

print("enter the number seperated by comma")
n=input()
print(n)
l=[int(e)*int(e) for e in n.split(',')]
print("square=",l)

n=input()
l=[int(e)for e in n.split(',')]
l.sort(reverse=True)
print(l)

#create a list from a given list by selecting only even places elements
n=input()
l=[int(e)for e in n.split(',')]
i=0
l1=[]
for e in l:
    if i%2==0:
       l1.append(e)
    i+=1
print("new list=",l1)