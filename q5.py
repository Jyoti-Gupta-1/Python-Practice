#Write a function to find maximum of three numbers in Python.
def maximum_num (v1,v2,v3):
    if v1>v2 and v1>v3:
        print(v1, "is the greatest number")
    elif v2>v1 and v2>v3 :
        print(v2,"is gretest number")
    else:
        print(v3,"is greatest number")
    
maximum_num(12,5,9)
    

# Write a Python function to create and print a list where the values are square of numbers between 1 and 30.
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
        
    return l

print(create_list())


# Write a Python function that takes a number as a parameter and check if the number is prime or not.
def check_prime (num):
    if num==1:
        print("it is not a prime number")
    if num==2:
        print("it is a prime number")
    if num>2:
        for i in range(2,num):
            if num%i==0:
                print("it is not a prime number")
                break
        else:
            print("it is a prime number")  
    
check_prime(11)

# Write a Python function to sum all the numbers in a list.
def sum(num):
    total =0
    for i in num:
        total+=i
    return(total)

print(sum([24,4,5,64,89]))

#solution 2(recursion)
def sum(num):
    if len(num)==1:
        return(num[0])
    else:
        return(num[0]+sum(num[1:]))
print(sum([24,4,5,64,89]))


# Write a Python program to solve the Fibonacci Sequence using Recursion
def fib(num):
    if num==1:
        return (0)
    if num==2:
        return (1)
    else:
        return(fib(num-1)+fib(num-2))
print(fib(7))