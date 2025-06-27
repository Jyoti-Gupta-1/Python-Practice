#find sum of all even numbers from 1 to 50

sum=0
for i in range (1,51):
    if i%2==0:
        sum+=i #add i to current value of sum
print("sum of 1 to 50 is:",sum)

#write a program to write first 20 numbers and there square number

for i in range(1,21):
    print(i , i**2)

#write a program to find sum of first 10 odd numbers using while loop

sum=0
n=0
while n<=20:      #10 odd numbers
    if n%2!=0:
        sum+=n    #add number to sum
    n+=1          #increment
print("sum is:", sum)

#write a program to check if a number is divisible by 8 and 12 up to 100 numbers

for i in range (1,101):
    if i%8==0 and i%12==0:
        print(i)

#write a program to create a billing system at supermarket

while True:              #nested loop is used
    name=input("enter your name:")
    total=0
    while True:
        print("enter amount and quantity")
        quantity=float(input("enter quantity:"))
        amount=float(input("enter amount:"))
        total+= amount*quantity
        repeat=input("do you want to add more items (yes/no)?")
        if repeat=="no":
            break

    print("-"*40)
    print("name:",name)
    print("amount to be paid:",total)
    print("-"*40)
    print("*****thank youuu********")

    repeat1=input("do you want to go to next customer (yes/no)?")
    if repeat1=="no":
        break
    else :
        continue


