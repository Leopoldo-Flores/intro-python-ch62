
print("Hello world form python!")
print(2)
print(2+3)
print(True) # dosent work

#This is a comment
""" 
This is a multi line comment
"""

# Create a variable
name = "Leopoldo"
age = 23
middle_name = "Javier"
last_name = "Flores"
found = False
print(name)

# concatination (putting things together)
print("My name is: " + name + ", and i am " + str(age) + " years old." + middle_name)
print("Did he show up to class?" + str(found))

# f format
# f""   f"""
print(f"My name is: {name}, and i am {age} years old")
print(f"""  
leo
      lalala
    middle{middle_name}
                printing

""")

# type() function helps us to know what type of data a variable is
print(type(name))
print(type(age))
print(type(found))

# casting
# helps us convert to different data types
print(20+int("20"))
print(20+age)

# input method
# is going to allow us to interact with the terminal and pass some variables
# print(input("Enter your name here: "))
# print(type(input("Enter your name here: ")))

# new_age = input("Enter your age here: ")
# print(new_age + age)
# print(str(age) + new_age)

x = int(input("enter first value: "))
y = int(input("enter second value: "))
print(x*y)
