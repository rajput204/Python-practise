#write a python script to print n odd natural number
def odd(n):
    for i in range(0,n+1):
        print(2*i+1,end=' ')
odd(10)
print( )

def prime(n):
    for i in range(1,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
prime(10)
print( )

def all_prime(beg,end):
    for i in range(beg,end+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
all_prime(1,20)
print( )

#n term of fibonacci series
def fibonacci(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
fibonacci(10)
print( )


#all factor's of a given number
def num(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')
num(4)
print( )

# def lcm(n,m):
#     i=1
#     while i<=n*m:
#         if (i%n==0 and i%m==0):
#             print(i)
#     i+=1
# lcm(4,6)

def string(s):
    count=0
    for i in range(len(s)):
        count+=1
    
    print(count,end=' ')
string('aditya')
print( )

l=[]
def prime1(n,e):
    for i in range(n,e+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
    print(l)
prime1(1,20)

def word(s):
    dict={}
    for i in s:
        first_letter=i[0].lower()
        if first_letter.isalpha():
            if first_letter in dict:
               dict[first_letter].append(i)
              
            else:
              dict[first_letter]=[i]
    for k,v in dict.items():
       print(k,v)
word(["patna","mumbai","chennai","delhi","rajasthan"])
print( )

def string(s):

      d={i[0]:i for i in s}
      print(d)
string(["patna","rajasthan","delhi"])

def string1(s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    d1={}
    for ch in alpha :
        l1=[word for word in  s.split(' ')if word.startswith(ch)]
        print(l1)
        if len(l1)>0:
         d1[ch]=l1 #assigning operator is used to assigning the value to the dictionary ch is the key and l value 
    return d1

print(string1("aditya is a good boy"))

print( )
def filter_and_group_by_alphabet(text):
    # Split the text into words
    words = text.split()

    # Create a dictionary to store results
    result_dict = {}

    # Iterate through each word in the text
    for word in words:
        # Ensure the word is not empty
        if len(word) > 0:
            # Get the first letter of the word (converted to lowercase for case-insensitivity)
            first_letter = word[0].lower()

            # Check if the first letter is an alphabet character
            if first_letter.isalpha():
                # If the first letter is not a key in the dictionary, create an empty list
                result_dict.setdefault(first_letter, [])

                # Append the word to the list corresponding to its first letter
                result_dict[first_letter].append(word)

    return result_dict

# Example usage:
text_example = "Hello world, how are you doing? Python programming is amazing!"
result = filter_and_group_by_alphabet(text_example)
print(result)

#factor of a number

def factor(a,b):
    l1=[]
    f=a if a<b else b
    while f>=1:
        if a%f==0 and b%f==0:
            l1.append(f)
        f-=1
    return tuple(l1)
print(factor(12,15))
print( )
