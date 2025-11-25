# Write a python program to sort a dictionary by value.

a={"a":12,"b":23,"c":6,"d":91,"e":45}
a=sorted(a.values())
print(a)

# Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.

a={}
for i in range (1,16):
    a[i]=i*i
print (a)


# Write a program to multiply all the items in a dictionary
a={"a":1,"b":2,"c":3,"d":4,"e":5}
mult=1
for i in a :
    mult *=a[i]
    
print (mult)


#write a python program to start a dictionary by key.
a= {12:"a", 56:"b",23:"c",48:"d",91:"e"}
a=dict(sorted(a.items()))
print(a)