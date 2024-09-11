# Dictionary - collection of data - mutable (changed) - keyed - key value pair

# List
names = ["John", "Jane", "Smith"]

# Dictionary
person1 = {
    "first_name": "John",
    "last_name": "LastName",
    "age": 27
}

print(person1)
print(person1["last_name"])
print(person1.get("first_name"))

# print(person1["address"])
print(person1.get("address", "No address"))

person1["address"] = "Australia"
print(person1)

person1["age"] = 29
print(person1)


# Loop
print("Loops starts from here: \n")
for key in person1:
    print(f"Key: {key}")
    print(f"Value: {person1[key]}\n")