# Lists are used to store MULTIPLE items in a single variable

my_list = [10, 20, 30, 40, 50]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing list items by their INDEX number
fruits = ["apple", 'bannana', "cherry"]
print(fruits[0])
print(fruits[2])

# You can also use NEGATIVE indexes to count from the end
print(fruits[-2])

# MODIFY the list
fruits[1] = "mango"
print(fruits)

# Adding to list
fruits.append("orange") # Adds to end of list
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

# Removing items
fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

# Check if item exists
if "mango" in fruits:
    print("Yes, mango is in list!")

# List length
print(len(fruits)) # Number of items in list