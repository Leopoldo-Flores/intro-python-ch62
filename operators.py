# operators are like "symbols" or "shortcuts"
# that tell the computer to do something with values 

# 1. Arithmetic operator- used with numeric values 
x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

res = x % y # Modulus-> remainder after division
print(res)

res = x ** y # Exponentation-> x to the power of y
print(res)

res = x // y # Floor division-> divide and drop the decimal
print(res)

print("__________________________________________________")
# 2. Assignment operators - used to assign values to variables
# = means "put this value inside the (variable)"

x = 5
x += 5
x -= 3
x *= 3
x /= 3
print(x)

print("__________________________________________________")
# 3. Comparison operator
# used to compare two values 
# same as if else
z = 5
p = 5
print(z == p) # equal to
print(z != p) # not equal to
print(z <= p) # less than/ greater than
print(z >= p)

print("__________________________________________________")
# 4. Logical operators
# used to compine conditional statements

x = 3
y = 10
z = 3

print(x == y and y ==z) # False, both conditions are NOT true
print(x == y or y ==z)  # True, at least one condition is ture
print(not x == y)       # True, because x == y is false, 

print("__________________________________________________")
# 5. Identity operator
# used to compare the objects, not if they are equal but if they
# are actually the same object with the same memory locaton

x = 3
y = 5
print(x is y) # Returns True if both variables are the same object
print(x is not y) # Returns True if both variables are not the same object

print("__________________________________________________")
# 6. Membership operator
# used to test is a sequence is presented in an object

x = [1, 2, 3, 4, 5] # this is a list

print(4 in x) # True, 4 is indide the list
print(9 not in x) # True, 9 is not in the list
