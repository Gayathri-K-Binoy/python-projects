# print("Hello, World!")

#Strings
name = "Silas"
#Integers
age=18
#Floats
height=12.4
#Booleans
is_student=False

# print("Hello,my name is "+name)
# print("Hello,my name is",name)

print(name[-1])

message="Hello world"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("l","L"))

print("World" in message)
#Python is case sensitive

print(len(message))

greeting1="Hii"
greeting2="hii"
if greeting1==greeting2:
    print("Same")
else:
    print("Different")

#Type conversion
age_str="30"
age_int=int(age_str)
print(type(age_str))
print(type(age_int))

price_float=45.7
price_int=int(price_float)
print(price_int)