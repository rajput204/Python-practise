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

s={'dhoni','anuj','virat','jadeja','gambhir'}
for e in s:
    for f in list(s)[1::]:
        print(e,f)
print( )

l=list(s)
for e in s:
    for f in l[1::]:
        print(e,f)

print( )

candidates={"arun","atishay","priyam","pankaj","harish","anita","sohail","rahul","deepak","rajesh","gurpreet"}
black_hat_candidates={"priyan","deepak","harish","anita","rahul","rajesh"}
red_shoes_candidates={"arjun","pankaj","priyan","rahul","gurpreet"}
s1=black_hat_candidates.intersection(red_shoes_candidates)
print(s1)
print( )
for e in s1:
    print(e)
print( )

n=int(input("enter the sum of dice numbers"))
p=set()
for i in range(1,7):
    for j in range(1,7):
        if i+j==n:
            p.add((i,j))
print(p)








