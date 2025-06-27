#string slicing

a="1234567890"

print(a[0:3])  #123
print(a[::2]) # gap of 2
print(a[:5])
print(a[-5:])
print(a[::-1])
print(a[6::-1])

#write a program to get fibonacci series upto 10 numbers
#0,1,2,3,5,8

a=0
b=1
for i in range(1,6):
    c=a+b
    a=b
    b=c
    print(c)

#user input

a=0
b=1
n=int(input("enter the number:"))
if n==1:
    print(1)
else:
    for i in range(2,n):
         c=a+b
         a=b
         b=c
         print(c)


#wrie a program to check if a number is prime or not

n=int(input("enter the number:"))
if n%n==0 or n%1==n:
        print("the number is not prime ")
else:
        print("the number is prime")

#OR
n=int(input("enter the number:"))
if n<=1:
    print("it is not a prime")
else :
    for i in range(2,n):
        if n%i==0 :
            print("the number is not prime ")
            break
    else:
            print("the number is prime")


#write a program to find a palindrome of string

n=input("enter the number/word")
m=n[::-1]
if n==m:
    print("it is palindrome")
else :
    print("it is not a palindrome")

#write a program to find a palindrome of integer

n = int(input("Enter the number: "))
original = n     #stored original number
reverse = 0      #used to store reverse of number

while n > 0:
    digit = n % 10                     #this gives last digit of the mumber
    reverse = reverse * 10 + digit     #reverse = 0 * 10 + 3 = 3, reverse = 3 * 10 + 2 = 32
    n = n // 10                        #this removes the last digits from number

if original == reverse:
    print("The number is a palindrome")
else:
    print("Not a palindrome")


#write a program to create an area calculator using loop

print(" AREAAA CALCULATORRRR")

while True:
    print(""" PRESS 1 TO GET AREA OF SQUARE
      PRESS 2 TO GET AREA OF RECTAGLE
      PRESS 3 TO GET AREA OF CIRCLE
      PRESS 4 TO GET ARAE OF TRIANGLE
      """)

    choice=int(input("enter your choice betweem 1-4 :"))

    if choice==1:
        while True:
            side= float(input("enter the length of side:"))
            area=side**2
            print("area of square is: ",area)
            repeat=input("do you wanna try again with square? yes/no: ")
            if repeat=="no":
                break
            
    elif choice==2:
        while True:
            l=float(input("enter length : "))
            b=float(input("enter breadth : "))
            area=l*b
            print("area of rectangle is:",area)
            repeat=input("do you wanna try again with reactangle? yes/no: ")
            if repeat=="no":
                break

    elif choice==3:
        while True:
            r=float(input("enter the radius :"))
            area=(22/7)*r**2
            print("the area of circle is:",area)
            repeat=input("do you wanna try again with circle? yes/no: ")
            if repeat=="no":
                break

    elif choice==4:
        while True:
            
            b=float(input("enter base : "))
            h=float(input("enter height : "))
            area=(1/2)*b*h
            print("the area of triangle is:",area)
            repeat=input("do you wanna try again with triangle? yes/no: ")
            if repeat=="no":
                break

    repeat1=input("do you wanna repeat it? yes/no: ")
    if repeat1=="no":
        break
