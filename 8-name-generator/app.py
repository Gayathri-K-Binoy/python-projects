import random
print("FANTASY NAME GENERATOR")

num=int(input("How many names do you want? "))
first_parts=["Moon","Winds","Sun","Star","Sea","Sun","Water","Fire","Ice"]
last_parts=["dancer","singer","walker","reader","rider","player","seeker","keeper","hunter"]
for _ in range(num):
    first_name=random.choice(first_parts)
    last_name=random.choice(last_parts)
    print(f"{first_name}{last_name}")
