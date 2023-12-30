x=input("enter the string")
alpha="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
for e in x:
    if e in alpha:
         print(True)
    else:
      print(False)
print( )

x=input("enter the string")
vowels="a,e,i,o,u,A,E,I,O,U"
count=0
for e in x:
    if e in vowels:
        count+=1
print("vowel count=",count)
print()

#couting the alphabets
x=input("enter the string:")
count=0
for e in x:
    count+=1
print("count of alphabet=",count) 
print( )

#string reversal
s=input("enter the string")
print(s[::-1])
print( )




     