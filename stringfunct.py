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
