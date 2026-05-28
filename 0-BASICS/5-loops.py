print("Counting from 1 to 5")
for i in range(1,6):
    print(i)
print("\nCounting from 5 to 1")
for i in range(5,0,-1):
    print(i)
#While loops
cnt=1
while cnt<=5:
    print(cnt)
    cnt+=1
#reversed while loop
cnt=5
print("\nReversed while loop")
while cnt>=1:
    print(cnt)
    cnt-=1

#Looping through a list
fruits=["apple","banana","cherry"]
print("My fruits:")
for fruit in fruits:
    print(fruit)
    
#Reversing a List
print("\n My fruits in reverse:")
for fruit in reversed(fruits):
    print(fruit)

#Loop with enumerate
print("fruit with indices:")
for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

#Loop with dictionaries
person={"name":"Jane","age":23,"city":"LA"}
print("\nPerson dictionary")
for key,value in person.items():
    print(f"{key}:{value}")

#List comprehension (Compacct loop for creating lists)
squares=[x**2 for x in range(1,6)]#[1,4,9,16,25]
print ("Squares from 1 to 5",squares)

#fruits=["apple","banana","cherry"]
#for loop with zip()-iterate through multiple lists in parallel
colors=["Red","Yellow","Green"]
print("\nFruits ans their colors")
for fruit,color in zip(fruits,colors):
    print(f"{fruit} is {color}")


#break and continue
print("\n Loop with a break")
for i in range(1,10):
    if i>5:
        break
    print(i)

print("\n loop with continue")
for i in range(1,10):
    if i%2==0:
        continue#skip even numbers
    print(i)

#infinite loop with break condition
i=1
print("\n controlled infinite loop")
while True:
    print(i)
    i+=1
    if i>5:
        break
