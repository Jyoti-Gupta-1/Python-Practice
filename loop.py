#for loop

for i in range(1,8):
    print("hellooo")
print()
for i in range(1,8):
    print(i) #prints 1 to 7 numbers
print()
for i in range(1,8,2):
    print(i) #prints alternative numbers(odd)
print()
for i in range(0,8,2):
    print(i) #prints even numbers
print()


#print a multiplication table using for

num=int (input("enter the number: "))
for i in range (1,11):
    print(num ,"x", i ,"=" ,num*i)


#while loop

num=int(input("enter the number:"))
while num<=50:
    print(num)
    num+=1


#multiplication table using while
n=2
num=int(input("enter the number: "))
while n<=10:
    print(num ,"x", n, "=", num*n)
    n+=1


#while True loop
while True:
    num1=int(input("enter the 1st number: "))
    num2=int(input("enter the 2nd number: "))
    print(num1+num2)

    repeat=input("do you want to stop(yes/no)")
    if repeat=="yes":
        break


#nested loop

for i in range(1,4):
    for j in range(1,3):
        print(j ,end="") 
    print(i)


"""solving patterns:
 1
 12
 123
 1234
 12345"""

for i in range(1,6):
    for j in range (1,i+1):
        print(j, end="")
    print()


#for loop with conditional statement
#for finding common multiples of two numbers

for i in range(1,100):
    if i % 4 == 0 and i % 3 == 0:
        print(i)


 #while loop with conditional statement

n=1
while n<=10:
    if n==3:
        print("add to fav song")
    else:
        print(n)
    n+=1


#break and continue statement

#use of continue

for i in range(1,11):
    if i==5: #it skips number 5 and then continues
        continue
    else:
        print(i)
        
#use of break

for i in range(1,11):
    if i==7: # prints only till 6 and doesnt go after 7
        break
    else:
        print(i)

    







