#booleans in python
# boolean data type has two values True and False

a = True
b = False
print(a) #this prints True
print(b) #this prints False

# we can use boolean values in conditional statements
if a:
    print("a is True")  #this prints a is True
else:
    print("a is False")     
if b:
    print("b is True")
else:
    print("b is False")  #this prints b is False

    x = 200
print(isinstance(x, int)) #this prints True because x is an integer
print(isinstance(x, str)) #this prints False because x is not a string

# we can use boolean values in logical operations
print(a and b) #this prints False because a is True and b is False  

print(a or b)  #this prints True because a is True or b is False

print(not a)  #this prints False because not True is False
print(not b)  #this prints True because not False is True

# we can convert other data types to boolean using bool() function
print(bool(1))  #this prints True because 1 is considered as True
print(bool(0))  #this prints False because 0 is considered as False
print(bool("Hello"))  #this prints True because non-empty string is considered as True