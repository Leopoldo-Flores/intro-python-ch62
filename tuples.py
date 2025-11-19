# Tuples are just like lists - they can store multiple items.
# BUT!!! Tuples are IMUTABLE (you can't change them after creation)

my_tuple = ("apple", "banna", "cherry")
print(my_tuple)

# Accessing items
print(my_tuple[0])
print(my_tuple[2])

# check if item exists
if "cherry" in my_tuple:
    print("Yes it is")

#length of tuple
print(len(my_tuple))

# single item tuple
# You must add a comma at the end to recognize as a tuple
single = ("apple")   # this is just a string
print(type(single)) 
correct = ("apple",) # this is a tuple
print(type(correct)) 

# Nested tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1,tuple2)
print(combine)
