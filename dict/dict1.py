#find the square of n natural number are keys and the squares are data values
n=int(input("enter the range of the number"))
d={e:e**2 for e in range(1,n+1)}
print(d)

#sort the dictionary by it keys in descending order
l1=sorted(d,reverse=True)
for k in l1:
    print(k,' ',d[k])
print( )


#python script to create the dictionary where the key values in the dictionary are batch codes and data values are size of the batch
d={"sa":200,"sb":250,"sc":112,}
max=0
for k,v in d.items():
    if v>max:
        max=v
print(max)
print( )

l=["jaipur","ambala","jajpur","gurgaw","chennai","champaran","darbhanga","noida"]
d={}
for city in l:
    first_letter=city[0].lower()
    if first_letter.isalpha():
        if first_letter in l:
            d[first_letter].append(l)
            break
        else:
            d[first_letter]=[city]
for k,v in d.items():
    print(k,v)
print( )

n=int(input("how many players u want to store"))
print("enter name of thr player")
players={}
for i in range(1,n+1):
    name=input("enter the name of the player")
    print("enter the match played")
    a=input()
    print("total run")
    b=input()
    print("half centuries")
    c=input()
    print("centuries")
    d=input()
    players[name]=(a,b,c,d)
for k,v in players.items():
    print(k,v)
 


