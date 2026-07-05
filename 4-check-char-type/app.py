print("CHARACTER TYPE CHECKER")
ch=input("Enter a single character: ")

if ch.isalpha():
    print("This is a letter.")
elif ch.isdigit():
    print("This is a number.")
else:
    print("This is a special character.")