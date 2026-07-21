print("REVERSE NAME GENERATOR")

while True:
    name=input('Enter a name: ')
    if not name:
        break
    rev_name=name[::-1]
    print(f"Your reversed name is: {rev_name}")
    print(f"In a parallel universe, they call you {rev_name.capitalize()} !")
    choice= input("\nTry another name? (y/n): ")
    if choice.lower()!='y':
        break

