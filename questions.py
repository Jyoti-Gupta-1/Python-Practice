
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
