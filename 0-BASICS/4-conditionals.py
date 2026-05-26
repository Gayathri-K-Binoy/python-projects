#Python uses indentation to define blocks of code, not curly braces or other symbols
temp=28
if temp>30:
    print("It's hot outside")
elif temp>20:
    print("It's a nice day!")
else:
    print("It's cold outside")

#Checking multiple conditions with logical operators
age=24
has_license=True
if age>=18 and has_license:
    print("You can drive")
elif age>=18 and not has_license:
    print("Need license")
else:
    print("You are too young")

#Nested conditionals
score=85
if score>=60:
    print("You passed!")
    if score>=90:
        print("A grade")
    elif score>=80:
        print("B grade")
    elif score>=70:
        print("C grade")
    else:
        print("D grade")
else:
    print("You failed")


#using "in" operator with conditionals
fruit="apple"
if fruit in ["apple","banana","mango"]:
    print(f"{fruit} is there in list")

#Ternary operator (1-line if-else)
age=20
status="Adult" if age>=18 else "Minor"
print(f"Status: {status}")

#comparing strings
password="password123"
if password=="password123":
    print("Access granted!")
else:
    pass #skips for later

#Chaining comparisons
x=15
if 10<x<20:
    print("x is between 10 and 20")

#Truthy or falsy
user_input=""
if user_input:
    print("Input given")
else:
    print("No input given")