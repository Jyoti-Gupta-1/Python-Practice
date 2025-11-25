"""a="apple","banana","cherry",1,3.44
print(type(a))

#when using only one element
b="apple",  #add a comma for making it str to tuple
print(type(b))

#for adding anything in tuple , first convert it into list and append. then convert it back to tuple
a=list(a)
a.append("chashni")
print(a)
a=tuple(a)
print(a)

a.pop(4)
print(a)