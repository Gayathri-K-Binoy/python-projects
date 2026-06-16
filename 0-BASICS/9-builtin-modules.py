import random
import math
import datetime
import os
import sys
import time

#Get random number
random_number=random.randint(1,10)#1 and 10 is included
print(f"Random number is {random_number}")

#choose a random element from the list
fruits=["apple","banana","mango","cherry","peach"]
random_element=random.choice(fruits)
print(f"random fruit is {random_element}")

#shuffle the list
random.shuffle(fruits)
print(fruits)

#math module
print(f"Square root of 16 is {math.sqrt(16)}")
print(f"Pi is {math.pi}")
print(f"Ceiling of 4.2 is {math.ceil(4.2)}")
print(f"Floor of 4.7 is {math.floor(4.7)}")
print(f"5 raised to 3  is: {math.pow(5,3)}")

#datetime module
current_time=datetime.datetime.now()
print(f"Current date and time is {current_time}")
print(f"Todays date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().year}")#day month year

#OS module
current_directory=os.getcwd()
print(f"Current directory: {current_directory}")
print(f"List of files: {os.listdir('.')}")
print(f"List of files: {os.listdir()}")

#Time module
print("Waiting for 2 seconds..")
time.sleep(2)
print("Done!")

#Sys module
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")#eg: 'win32','darwin','linux'