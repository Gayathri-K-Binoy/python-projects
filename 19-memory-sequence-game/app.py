import random
import time
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name=="nt" else "clear")

print("MEMORY SEQUENCE GAME")
print("Remember the sequence and type it back! ")
print("\n Rules:")
print("Watch as numbers appear one by one")
print("After the sequence is shown, type it back in order")
print("Each round adds one more number to remember")
print("How far can you go?")

input("Press Enter to start...")