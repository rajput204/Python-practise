#write a python script  to convert a number into str type
x=19
print(type(str(x)))

x='m'
print(ord(x)) #unicode of  m is 109
print()
x=100
print(chr(x)) #cahracter of 100 is d

x='256'
print(type(int(x)))
print()
#it will not possible when it contains both character and interger
x='a45'
print()
x=124
print()
print(type(x))
print(type(bool(x)))
#note:- ord is used to get the unicode of the character and chr is used to convert the character of the number