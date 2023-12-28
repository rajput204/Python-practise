from emoji import emojize
# x=input("enter the string")
# for e in x:
#   print(e,ord(e))
# print(emojize(":thumbs_up:")*10)

# x=input("enter the string")
# vowels="a","e","i","o","u"
# for e in x:
#   if e in vowels:
#     print (e,end=" ")
# print("\u2764\ufe0f"*10)

# x=input("enter the string")
# count=0
# for e in x:
#   if ord(e)==32:
#     count+=1
# print("number of space=",count)

x=str(input("enter the number"))
i=0
for e in x:
  if x.index(e)==i:
    print(e,end=" ")
  i+=1
print( )
print("\u2764\ufe0f"*12)

x=input("enter the number")
count=0
for e in x:
  count+=1
print(count)
  
  


