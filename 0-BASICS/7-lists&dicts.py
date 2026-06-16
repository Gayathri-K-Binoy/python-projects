#Lists are collections of items that can store different types of data

numbers=[1,2,3,4,5,3,3]
print(numbers)

print(numbers[0])
numbers[1]=22
numbers.remove(3)
numbers.append(44)
print(numbers)

print(len(numbers))
#Slicing lists 
numbers=[1,2,3,4,5]
print(numbers[1:4])#Print elements from index 1 to 3
print(numbers[::2])#every other element: start,stop,step
print(numbers[1::2])#every other element: start,stop,step
print(numbers[::-1])#reverse list
print(numbers+[6,7,8])#concatenate list
print(numbers*3)#repeat the list

#Dictionaries are collections that store data as key-value pairs
student={
    "name":"Rachel",
    "age":22,
    "courses":["Math","CS"]
}
print(student["name"])
student["grade"]="B"
student["age"]+=3
print(student)

print(student.keys())
print(student.values())
print(student.items())

for k,v in student.items():#key, value
    print(f"{k}: {v}")

#Sets are unordered collection of unique items. - No duplicates allowed
unique_colors={"red","blue","green","pink","pink"}
print(unique_colors)

#Tuples are ordered collections that cannot be changed after creation
coordinates=(10.4,"e",12.3)
print(coordinates)
