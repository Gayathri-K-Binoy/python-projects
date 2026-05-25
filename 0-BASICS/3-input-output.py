name=input("Enter your name: ")
print(f"Hi, {name}")

age=int(input("Enter your age "))
age_to_100=100-age
print(f"You will 100 in {age_to_100} years")

num_1=float(input("Enter 1st number"))
num_2=float(input("Enter 2nd number"))
sum=num_1+num_2
print(f"Sum of {num_1} and {num_2} is {sum}")

#Working with multiple inputs in one line
x,y=input("Enter 2 numbers separated by a space: ").split()
print(f"First num is {x} and second number is {y}")

user_choice=input("Choose a color (or press Enter for default): ")
if user_choice=="":
    user_choice="blue"
print(f"Selected color : {user_choice}")

#endless possibilities
length=float(input("Enter length in meters: "))
print(f"Length in cms is {length*100}")