import time

print("COUNTDOWN TIMER")
print("Count down from your chosen seconds\n")

while True:
    try:
        seconds=int(input("Enter seconds to countdown from: "))

        if seconds<=0:
            print("Please enter a positive number")
            continue
        print(f"\nStarting countdown from {seconds} seconds!")
        for i in range(seconds,0,-1):
            print(f"{i} seconds remaining..")
            time.sleep(1)

        print("\nCOUNTDOWN COMPLETE!")
        start_over=input(f"Start another countdown? (yes/no): ").lower()
        if not start_over.startswith("y"):
            print("Thanks for using the countdown timer!")
            break
    except ValueError:
        print("Please enter a number.")