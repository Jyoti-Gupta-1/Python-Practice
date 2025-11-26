 #parameters and arguments
 
def add(x,y): 
    print(x+y)
       
add (12,34)

# arbitary argument

def hello(*name):
    print("hello, my name is",name[0])

hello("prathu","shweti","pranju")

#return function
def hello():
    return("helloo world")
print(hello())

def add(a,b):
    return(a+b)
print(add(12,4))

"""#recursion (calls itself)
def hello():
    print("hello")
    return (hello)
print(hello())"""

#factorial sum

def fact (n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
print(fact(4))

#lambda function

a=lambda b: b*5
print(a(4))

x=lambda a,b,c:(a+b)*c
print(x(3,10,3))

#local variables
x=24
print
def hello():
    global x
    x=25
    return x
print(hello())

print(x)
