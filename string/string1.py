#string is an iterable
#it is immutable.
#it is sequenced
#it can be of heterogenous type.
#it is a class

s1="aditya"
print(s1[1:6:1]) #output =ditya
print(s1[::1])#output=aditya
print(s1[::-1])#aytida this is slicing operator i.e [beg:end:diff]
print(s1[-2]) #negative indexing starts from back i.e starts from -1 output=y
print(s1[1])#from positive side count of index starts from 0 output=d

#method to access the string
#1.through index
#2.throung loop
#3.slicing operator

#string built in method
#min()
#max()
#len()
#sum()
#sorted()

#string object method
#split():-it return the list of the string.
#join():-it convert the list to string.
#is upper():-to check whether the string has upper case.
#is lower():-to check the lower case in string.
#is digit():-to check whether there is digit or not.
#upper():to convert the string the string to upper case.
#lower():-to convert the string to the lower case.
#index():-index of particular string.
#count():-count the number of string.
#startswith():-it check the starting of the string.
#endswith():- it check the ending of the string.
#replace():-to replace something with another by giving the entity s.replace('c','C') it will replace small with capital.
#casefold():-to check whether the string is uppercase or lowercase.


#it has both concatination operator and comaprison and repetation operator
s1="abc"
s2="cde"
print(s1+s2) #abccde

s1="abc"*3
print(s1)# abcabcabc

s1="aditya"
s2="ramesh"
print(s1<s2) #it will compare every alphabet order which will comes first will be smaller  further checking of the next string it works basically on the dictionary order





