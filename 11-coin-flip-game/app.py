import random

print("COIN FLIP GAME")
print("Guess heads or tails!\n")

while True:
    guess=input("Enter your guess (heads/tails) : ")
    if guess.lower()!="heads" and guess.lower()!="tails":
        print("Please enter 'heads' or 'tails'\n")
        continue #continue goes back to start of the loop

    flip=random.choice(["heads","tails"])
    print("The coin shows:",flip,"\n")
    if guess.lower()==flip:
        print('You guessed correctly! You win!\n')
    else:
        print('Sorry, wrong guess. Try again!\n')
    again=input("Play again? (yes/no): ")
    if not again.lower().startswith("y"):
        print("Goodbye!")
        break

