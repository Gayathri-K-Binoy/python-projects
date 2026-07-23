import random
print("WORD SCRAMBLE GAME")
print("Unscramble the letters to find the word!")

word_bank=["learn","python","happy","universe","music","garden"]

while True:
    random_word_str=random.choice(word_bank)
    random_word_list=list(random_word_str)
    random.shuffle(random_word_list)
    scrambled="".join(random_word_list)
    print(f"\nScrambled word: {scrambled}")
    if input("What's the word? ").lower().strip() ==random_word_str:
        print("Correct! You win!")
    else:
        print(f"Sorry, the word was: {random_word_str}")

    if not input("\nPlay again? (yes/no) ").lower().startswith("y"):
        print("Thanks for playing!")
        break


