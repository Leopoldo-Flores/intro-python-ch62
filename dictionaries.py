# Dictionaries store data in KEY:VALUE pairs {}

students = {
    "name": "Leo",
    "age": 22,
    "major": "computer science"
}

print(students)

# Accessing items
print(students["name"])      # Access by key
print(students.get("major")) # Access another way (.get)

# Add new item
students["graduation_year"] = 2025
print(students)

# Changing Values
students["age"] = 23
print(students)

# Remove item
students.pop("major") # Removes major
print(students)

# Check if KEY exists
if "height" in students:
    print("Key 'name' is in the dictionary")

# Nested dictionary
stuedents = {
    "student1": {"name": "leo", "age": 20},
    "student2": {"name": "alex", "age": 30}
}
print(stuedents["student1"]["name"]) # Access nested value