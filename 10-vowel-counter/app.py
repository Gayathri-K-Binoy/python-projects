print("VOWEL COUNTER")
#Simple syntax

# while True:
#     inp=input("\nEnter some text(or 'quit'): ")
#     if inp.lower()=="quit":
#         break
#     vowel_count=0
#     for letter in inp:
#         if letter.lower() in ['a','e','i','o','u']:
#             vowel_count+=1
        
#     print(f"That text has {vowel_count} vowels!")

#Advanced syntax
while True:
    inp=input("\nEnter some text(or 'quit'): ")

    if inp.lower()=="quit":
        break
    vowels=sum(1 for letter in inp if letter.lower() in "aeiou")
    print(f"That text has {vowels} vowels!")