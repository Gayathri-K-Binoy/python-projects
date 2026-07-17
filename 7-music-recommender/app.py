import random

print("MUSIC RECOMMENDER")
genres={
    "rock":["AC/DC","Ledd Zeppelin","Queen"],
    "pop":["Taylor Swift","Ariana Grande","Ed Sheeran"],
    "hip-hop":["Kendrick Lamar","Drake","J. Cole"]
}
choic=input("What genre do you like? (pop/rock/hip-hop): ")
if choic not in genres:
    print("Sorry,I am not aware of that genre.")
else:
    print(f"Check out {random.choice(genres[choic])}")