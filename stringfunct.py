#string functions

a="hello"
b="hello1234"
c="123    4567"
d="   HELLOO"
e=" "
f="1,a,@,#"
g="8.760"

#isalnum- checks for alphanumeric
print(a.isalnum())     #true
print(e.isalnum())     #false
#isalpha
print(a.isalpha())     #true
#isdeicimal 
print(g.isdecimal())   #false bcoz it is considering . as dot not a decimal
print(f.isdigit())     #false
print(c.isdigit())     #true
print(b.isnumeric())   #false
print(a.islower())     #true
print(f.isupper())     #false
print(e.isspace())     #true
print(b.istitle())     #false
print()
#some more

print(a.endswith("o"))
print(d.startswith("h"))
print(b.swapcase())
print(d.strip(" "))
print(f.split(","))
print(a.ljust(10,"*"))
print(b.rjust(20,"&"))
print(a.rindex("o"))
print(a.find("o"))
print(a.replace("hello","lata")) 

#write a program to sort string in asc order

n=input("enter anything:")
z=sorted(n)
print(z)

#count
y="sea is seaing after sea of the "
b=y.count("sea")
print(b)

#reversing

user="hello"
print("reverse is:", user[::-1])

#checking for only digits   # in digits only numbers are allowed
a=input("enter anything: ")
b=a.isdigit()
if b is True:
    print("it is digit")
else:
    print("it is not digit")
    
#program to find number of vowels in string

s=input("enter  string: ")
vowel_count=0
s=s.lower()
vowel="aeiou"
for i in s:
    if i in vowel:
        vowel_count+=1
print("vowel count is :",vowel_count)    

#check if every word in a string begins with a capital letter

s=input("enter input: ")
print(s.istitle())



