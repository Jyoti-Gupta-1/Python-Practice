"""a="apple","banana","cherry",1,3.44
print(type(a))

#when using only one element
b="apple",  #add a comma for making it str to tuple
print(type(b))

#for adding anything in tuple , first convert it into list and append. then convert it back to tuple
a=list(a)
a.append("chashni")
print(a)
a=tuple(a)
print(a)

a.pop(4)
print(a)


#1.Convert the following dictionary into JSON format (string).
import json
Student_data = {"name": "David", "age":13, "marks":87}
print(type(Student_data))
data =json.dumps(Student_data)
print(data)
print (type(data))"""

#2.Access the value of age from the given data.
import json
Student_data = """{"name": "David", "age":13, "marks":87}"""
data=json.loads(Student_data )
print(data["age"])

"""
#Pretty Print following JSON data 
Student _data = ("name": "David", "age":13, "marks":87) 
#Sort the following JSON keys and write them into a file
Student data = ("name": "David", "age":13, "marks": 8)"""