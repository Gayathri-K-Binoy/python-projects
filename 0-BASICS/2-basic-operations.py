import math
#basic operations
x=10
y=5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x%y)

#x=x+15
x+=15
print(x)

"""
CAMELCASE: firstName
SNAKECASE: first_name **
"""

#string concatenation
first_name="Jane"
last_name="Doe"
full_name=first_name+" "+last_name
print(full_name)


print("Hey my name is "+first_name+" and my last name is "+last_name)
#f strings
print(f"Hey my name is {first_name} and my last name is {last_name}")

#int floor division
a=17
b=3

print(a//b)#result 5(rounds down) normally it is 5.6(14 6's)7
print(a/b)

#assign multiple values
i,j,k= 10,20,30
print(i,j,k)

#swap values
m,n=1,2
n,m=m,n
print(m,n)

#comparisons operator
c=4
d=6
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>=d)
print(c<=d)

#logical operators
a=True
b=False

print(a and b)
print(a or b)
print(not b)

#string slicing
text="Python-programming"
print(text[0:6])
print(text[7:])
print(text[::-1])

#String formatting with .format()
name="Alice"
age=35
msg="My name is {} and my age is {} and i {}".format(name,age,4)
print(msg)

#using placeholders
msg1= "My name is {0} and my age is {1}. {0} is a cool name.".format(name,age,5)
print(msg1)

#math module operations
print(math.pi)#3.141592653589793
print(math.sqrt(16))#4.0
print(math.pow(3,4))#81.0
print(math.floor(3.5))#3
print(math.ceil(3.5))#4
num=3423.141592653589793
print(round(num,2))