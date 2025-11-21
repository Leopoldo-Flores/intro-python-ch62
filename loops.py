# WHILE LOOPS
# A while loops repeats a block of code as long as a condition is True
# Be carefule- if the condition never becomes False, youll get an INFINITE loop

count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1 # Assignment operator which adds one untill it equals to 5

print("--------------------------------")

# using break to stop the loop

count = 1

while count <= 10: # lopps until count is 10
    if count == 5: # checks when count is 5
        print("Break at 5!")
        break      # exits loop early
    print(count)
    count += 1

print("--------------------------------")

# using CONTINUE to skip and iteration

count = 0  # initialize count at 0

while count < 5:
    count += 1
    if count == 3:
        continue # skips 3
    print(count)

print("--------------------------------")

# Else with while
# The else block runs when the loop condition becomes False (not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop is finished!")

print("--------------------------------")

# FOR LOOPS
# A for loop is used for looping over a sequence:
# a list, tuple, dictionary, string, ect

# Loop through a list

fruits = ("apple", "banana", "cherry")
for fruit in fruits:  # for each fruit in the list fruits
    print(fruit)

print("--------------------------------")

# Loop though a string

for letter in "Hello":
    print(letter)

print("--------------------------------")

# Using range()
# range() generaes a sequence of numbers

for x in range(5):
    print(x)
print("--------------------------------")

# Start and end range
for x in range(2, 6):
    print(x)
print("--------------------------------")

# Step (skip numbers)
for x in range(0, 10, 2):
    print(x)

print("--------------------------------")

# Else in for loop
for x in range(3):
    print(x)
else:       # runs when loop is done
    print("loop is done")

print("--------------------------------")

# Break and Continue in for lops
for x in range(10):
    if x == 5:
        continue  # skips 5
    if x == 8:
        break     # stops loop at 8
    print(x)