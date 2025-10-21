# datatypes-string,integer,float,boolean
print("Hello"[0]) #string
print("Hello"[1])
print("Hello"[2])

print("123"+"345") #string conacatination
print(123+345)

print(3.14)#float

print(True)#boolean

#type()-function to know which type of datatype it is
print(type("Hello"))

print(type(123+345))

print(type(3.14))

print(type(True))

#typeconversion- convert data into different datatypes
number ="123" #string
print(type(number)) 

number =int("123") #converted to int
print(type(number)) 

#f-string: inserting a vartiable or an expression into a string
age = 22
print(f"Iam {age} years old")

name = input("enter your name?")
print(f"Iam {name} Tahreem")