
#checking if number is postive or not

num= int(input("enter the number :"))
if num>0:
    print("the number is positive ")
else:
    print("the number is negative")

#checking if number is odd or even

num= int(input("enter the number :"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#write a program to create area calcultor

print(" AREAAA CALCULATORRRR")

print(""" PRESS 1 TO GET AREA OF SQUARE
      PRESS 2 TO GET AREA OF RECTAGLE
      PRESS 3 TO GET AREA OF CIRCLE
      PRESS 4 TO GET ARAE OF TRIANGLE
      """)

choice=int(input("enter your choice betweem 1-4 :"))

if choice==1:
    side= float(input("enter the length of side:"))
    area=side**2
    print("area of square is: ",area)

elif choice==2:
    l=float(input("enter length : "))
    b=float(input("enter breadth : "))
    area=l*b
    print("area of rectangle is:",area)

elif choice==3:
    r=float(input("enter the radius :"))
    area=(22/7)*r**2
    print("the area of cicle is:",area)

elif choice==4:
    b=float(input("enter base : "))
    h=float(input("enter height : "))
    area=(1/2)*b*h
    print("the area of triangle is:",area)

else:
    print("invalid choice")

#check weather a letter is vowel or not
 
letter =input("enter a letter: ")
if (letter in"aeiou") or (letter in "AEIOU"):
    print("its a vowel")
else:
    print("not a vowel")

#check weather a umber is 2 digit ,3 digit or so on upto 5 digits

num=int(input("enter the number: "))
if num>=0 and num<=9:
    print("its a single digit number")
elif num>=10 and num<=99:
    print("the number is 2 digit ")
elif num>=100 and num<=999:
    print("the number is 3 digit ")
elif num>=1000  and num<=9999:
    print("the number is 4 digit ")
elif num>=10000 and num<=99999:
    print("the number is 5 digit ")
else:
    print("invalid")
