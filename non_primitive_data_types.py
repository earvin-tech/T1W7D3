# List - collection of data - mutable(changed) - indexed

names = ["John", "Jane", "Smith"]
#           0       1       2

names.append("Steve")
print(names)

names.pop()
print(names)

names[1] = "Somethiong else"
print(names)


# Tuple - collection of data - immutable (cannot be changed) - indexed

days = ("Monday", "Tuesday", "Wednesday")


# days.append("Thursday")

print(days[2])


# Set - collection of data - mutable (changed) - not indexed - no repeated items

names_set = {"John", "Jane", "Stacy", "Mike"}

# print(names_set[1])
names_set.add("Smith")
print(names_set)

names_set.remove("John")
print(names_set)

names_set.add("Jane")
print(names_set)


set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}

u = set1.union(set2)
print(u)

i = set1.intersection(set2)
print(i)

adb = set1.difference(set2)
print(adb)

bda = set2.difference(set1)
print(bda)