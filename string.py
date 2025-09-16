#string in python is a sequence of characters
# we can use single quotes or double quotes to represent string in python
a = "Hello, World!"
print(a) #this prints Hello, World!

# Taking input from the user
name = input("Enter your name: ")

# Printing the original string
print("Original String:", name)

# Converting the string to uppercase
uppercase_name = name.upper()
print("Uppercase:", uppercase_name)

# Converting the string to lowercase
lowercase_name = name.lower()
print("Lowercase:", lowercase_name)

# Finding the length of the string
length = len(name)
print("Length of the string:", length)

# Accessing first and last character of the string
print("First character:", name[0])       # index starts from 0
print("Last character:", name[-1])       # negative index gives last element

# Reversing the string using slicing
reversed_name = name[::-1]
print("Reversed String:", reversed_name)

#formatting the string using f-string
age = input("Enter your age: ")
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# Checking if the string is palindrome
if name.lower() == reversed_name.lower():
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")

# Escape characters in string
# To include special characters in a string, we use escape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

#string methods
# there are many string methods in python like (strip(), replace(), split(), join(), find(), index(), count(), isalpha(), isdigit(), isspace(), startswith(), endswith())
# we can use these methods to manipulate strings

# In python we have different data types like (text type, numeric type, sequence type, mapping type, set type, boolean type, binary type)
# we can get the data type of any object by using type() function
x="hello"
print(type(x)) #this prints <class 'str'> which means x is a string data type