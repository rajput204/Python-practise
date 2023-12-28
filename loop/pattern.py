x=int(input("enter the number of row's"))
for i in range(1,x+1):
    for j in range(1,x+1):
        print("*",end=" ")
    print(" ")



"""
output

* * * * *  
* * * * *  
* * * * *  
* * * * *  
* * * * * 
"""




x=int(input("enter the number of row's"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
output:-
* 
* * 
* * * 
* * * * 
* * * * * """
n=int(input("enter the number of elements"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end=" ")
    k=k+2
    print()
"""
* 
* * * 
* * * * * 
* * * * * * *
 """



    