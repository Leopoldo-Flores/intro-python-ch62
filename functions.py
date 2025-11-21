# It is a block of code which only runs when its called

# Simple function without parameters
def my_function():               # This is the function
    print("this is my function") # this line runs when function is called

my_function() # calling the function

def other_function():
    print("This is my other function")
other_function()

# Functions with parameters
def print_full_name(fname, last_name):
    print(f"This name is: {fname} {last_name} ")

ful_name = print_full_name("Leo", "Flores")

def full_name(fname, lname, mname):
    return f"{fname} {lname} {mname}"

# Store the returned value into a variable
name = full_name("Leo", "Flores", "javier") 
print(name)

