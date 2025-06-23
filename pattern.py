"""solving patterns:
 1
 12
 123
 1234
 12345"""

for i in range(1,6):
    for j in range (1,i+1):
        print(j, end=" ")
    print()

"""pattern:
1
22
333
4444
55555"""

for i in range (1,6):
    for j in range(1,i+1):
        print(i,end=" ")         #the only difference is j-->i
    print()


"""pattern:
11111
2222
333
44
5"""

for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")
    print()

"""pattern:
    *
   **
  ***
 ****
*****   """

for i in range(1,6):
    for j in range(5,i,-1):
        print("",end =" ")
    for k in range(i):
        print("*",end="")
    print()

"""pattern:
1
21
321
4321
54321"""

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""pattern:
*
**
***
****
*****
****
***
**
*     """

for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for k in range(0,i-1):
        print("*",end=" ")
    print()

"pattern:"
"1"
"2 4"
"3 6 9"
"4 8 12 16"
"5 10 15 20 25"
"6 12 18 24 30 36"

for i in range(1,7):
    for j in range (1,i+1):
        print(i*j,end=" ")
    print()

