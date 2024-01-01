#write the python script to print all distinct elements of a list.use set to solve the problem.
l=[10,20,30,20,30,10]
for e in set(l):
    print(e)

#create two set from a given set of number to seprate even and odd number
s1=set()
s2=set()
s={10,1,2,3,4,5,6,7,8,9,11}
for e in s:
    if e%2==0:
        s1.add(e)
       
    else:
        s2.add(e)
print(s1)
print(s2)









