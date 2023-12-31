s=["places","white","fly","sky","butters"]
count=0
for e in s:
    if e.endswith('s'):
       count+=1
print(count)

#to find the first repeated string of the list
l=["aditya","anshuli","aditya","anita","sunita","anita","sunita"]
i=0
for e in l:
    if e.index(e)!=i:
        print("first repeated string at index",e,i)
    i+=1

#sort the list of the string
l=["aditya","anuj","nitin","kajal","vinay","rohit"]
l.sort()
print(l)#it will change the existing list  ranther than creating the new list

#frequencies of occurance within  the string
l=[20,20,40,50,60,70,10,10]
i=0
for e in l:
    if l[i]==e:
       print(e ," ",l.count(e))
    i+=1



