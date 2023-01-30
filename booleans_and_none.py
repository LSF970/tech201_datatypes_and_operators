# Booleans

# True or False

# a = True
# b = False
#
# print(a == b) # False
# print(a != b) # True
# print(a >= True) # True
# print(b <= False) # True

# print(True and False) # False
# print(False and True) # False
# print(False or True) # True

# Booleans are useful for quickly checking the state of something.
# The other area Booleans are relly useful are validating data types.

# Booleans with Data types

# hi = "Hello world!"
#
# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.isupper()) # False
# print(hi.endswith(" world!")) # True
# print(hi.startswith("Hello")) # True

# x = 0
# y = 10
# z = -15
#
# print(bool(x)) # False - 0 is always False
# print(bool(y)) # True
# print(bool(z)) # True

# None

# None == Null in a lot other languages

print(bool(None)) # False

x = None

print(x == False) # False
print(x == True) # False

# Checking if a variable is None

print(x == None) # direct comparison - more complex situation.
print(x is None) # Best practice for checking if something 'is None'

print(type(x)) # <class 'NoneType'>


