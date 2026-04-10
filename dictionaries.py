# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: John

# Adding new key-value pair
person["email"] = "john@example.com"

# Updating existing value
person["age"] = 31

# Removing key-value pair
del person["city"]

# Dictionary methods
print(person.keys())    # All keys
print(person.values())  # All values
print(person.items())   # Key-value pairs

# Iterating through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if key exists
if "name" in person:
    print("Name exists in dictionary")

# Getting value with default
age = person.get("age", "Not found")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}