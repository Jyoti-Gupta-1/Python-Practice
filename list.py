a=["apple","banana","berry","papaya"]
print(a[:2])
print(a[::2])
print(a[::-1]) #reverse
print(a[-3:])
print(a[-1:-4:-1])

#iteration using for loop
for i in a:
    print(i)
    
#iteration using for loop with range and length function

for i in range(len(a)):
    print(a[i])
    
#iteration using while loop
i=0
while i<(len(a)):
    print(a[i])
    i+=1
    
#using short hand for loop

[print (i) for i in a]  #square bracket is imp

#list methods 
#finding length of list
print(len(a))    #gives the number of elements
#occurence of a element
print(a.count("apple")) 

#add element
a.append("grapes")  #adds element at the end of list
print(a)
#to add to a specific location
a.insert(2,"cherry")
print(a)

#remove from a list
a.remove("berry")
print(a)

#pop method used when u only know the index

print(a.pop(3))
print(a)

#to create a copy of elemenets
b=[]
print(b)
b=a.copy()
print(b)

#to access any element
print(a.index("grapes"))

#to entend the list means to add another list into this
c=["mango","pineapple"]
a.extend(c)
print(a)

#to revere the list using reverse method
a.reverse()
print(a)

#to sort the list- gives ascending order

a.sort()
print(a)

#to clear all the data
a.clear()
print(a)

A=["ross","rachel","monica","joe"]
#write a program to swap first and fourth element
A[0],A[3]=A[3],A[0]
print(A)

#add new value at second position
A.insert(1,"phoebe")
print(A)

#delete a value from 3rd element
A.pop(2)
print(A)

B=[13,7,12,10]
#multiply all the numbers in the list
mul=1
for i in (B):
    mul*=i
print(mul)

# to get the largest and smallest number in the list
B.sort()
print(B)
print("the largest value is:",B[-1])
print("the smallest value is:",B[0])