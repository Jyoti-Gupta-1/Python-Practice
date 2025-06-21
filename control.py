#if statement

marks=90

if marks>80:
    print("you have scored good")

# if else statement

marks=40
if marks>35:
    print("pass")
else:
    print("fail")

#if-elif-else statement

marks=int(input("enetr your marks:"))
if marks>=80:
    print("outstanding")
elif marks> 60 and marks<80 :
    print("great")
else:
    print("improvement")

#nested if statement

marks= int(input("enetr your marks"))

if marks>90:
    print("you will get new phone ")
    if marks>=99:
        print("you can go on a trip")
else:
    print("no phone for a month")

# short hand if statement"""

marks=89

if marks>80 : print("goood")

# short hand if-else statement

marks=89

print("outstanding") if marks>90 else print("not greatt")



