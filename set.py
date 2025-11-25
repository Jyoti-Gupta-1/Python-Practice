#functions of sets

a={"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor"}

"""#isdisjoint
print (a.isdisjoint(b))  #gives true bcoz no element in B is same as in A

#issubset
print(a.issubset(c))

#issuperset
print(a.issuperset(c))  #A has all the elements of C

#update       #acts as union of both set
a.update(c)
print(a)

#clear
a.clear()
print(a)  #shows set A is empty
"""
#union (similar as update)
print(a.union(c))

#difference
print(a.difference(c))

#difference update
a.difference_update(c)
print(a)

#intersection
print(a.intersection(b))

#intersection update
#symmetric difference
#symmetric difference update

#problems
#Write a program to find max and min in a set.
a={12,12,23,34,56,78,98,9}
maximum=max(a)
minimum=min(a)
print("the min value is ", minimum)
print("the max value is ",maximum )

#Write a program to find common elements in three lists using sets.
a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]

print(set(a)& set(b)&set(c))


# Write a program to find difference between two sets.
a={1,5,6,8,2}
b={4,5,6,7}
print(a.difference(b))

# Write a Python program to remove an item from a set if it is present in the set.
a={1,5,6,8,2}
a.discard(8)
print(a)

# Write a Python program to check if a set is a subset of another set.
a={1,5,6,8,2}
b={1,5,6}
print(b.issubset(a))