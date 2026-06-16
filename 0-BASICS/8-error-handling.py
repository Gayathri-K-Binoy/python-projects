try:
    number=int(input("Enter a number "))
    res=10/number
    print(f"10 divided by {number} is {res}")
except ValueError:
    print("Thats not a valid number!")
except ZeroDivisionError:
    print("Cant divide by zero!")
except:
    print("Error occured")
finally:
    print("Always executed piece of code!")