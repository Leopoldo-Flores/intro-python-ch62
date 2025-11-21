# if -> checks the condition
# elif -> (else if) checks another condition if the first one is False
# else -> runs if all other conditions are False

x = -12

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand if statement - writing it all in one line

if x > 5: print("x is greaterthan 5")

# Short hand if...ELSE

print("even") if x % 2 == 0 else print("odd")

# Nested if statement
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# combining conditions
age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")