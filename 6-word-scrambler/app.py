import random

print("WORD SCRAMBLER")

while True:
    inp=input("\nEnter a word to scramble (or 'quit'): ")
    if inp.lower()=="quit":
        print("Goodbye!")
        break
    #String needs to be converted to list
    #"friend" to ["f","r","i","e","n","d"]
    # shuffle => ["f","r","i","e","n","d"] =["f","n","i","e","r","d"]
    #convert list to string
    word=list(inp)
    print(word)
    random.shuffle(word)
    print(word)
    print(f"Scrambled: {"".join(word)}")
