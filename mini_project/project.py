name1=input("enter the first name")
name2=input("enter the second name")
combined_name=name1+name2
lower_name=combined_name.lower()
t=lower_name.count('t')
r=lower_name.count('r')
u=lower_name.count('u')
e=lower_name.count('e')
first_digit=t+r+u+e
print(first_digit)
l=lower_name.count('l')
o=lower_name.count('o')
v=lower_name.count('v')
e=lower_name.count('e')
second_digit=l+o+v+e
print(second_digit)
count=int(str(first_digit))+int(str(second_digit))
if count<10 or count >90:
    print(f"your score is {count},you got together like coke and mentos.")
elif count>=40 and count<=50:
    print(f"your score is{count},you are alright together.")
else:
    print(f"your score is {count},")
