print("TEXT CAPITALIZER")
text=input("Enter some text here: ")
choice=int(input("1. UPPERCASE\n2. lowercase\n3. Title Case\n4. Sentence case\n Choose a format(1-4): "))
if choice==1:
    print(text.upper())
elif choice==2:
    print(text.lower())
elif choice==3:
    print(text.title())# title makes first letter of each word capitalized
else:
    print(text.capitalize()) #capitalize makes first letter of the first word capitalized.