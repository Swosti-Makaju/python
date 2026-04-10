# For Loop
print("--- For Loop ---")
for i in range(5):
    print(f"i = {i}")

# For Loop with List
print("\n--- For Loop with List ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
print("\n--- While Loop ---")
count = 0
while count < 3:
    print(f"count = {count}")
    count += 1

# Nested Loop
print("\n--- Nested Loop ---")
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

# Loop with Break
print("\n--- Loop with Break ---")
for i in range(5):
    if i == 3:
        break
    print(f"i = {i}")

# Loop with Continue
print("\n--- Loop with Continue ---")
for i in range(5):
    if i == 2:
        continue
    print(f"i = {i}")

# List Comprehension
print("\n--- List Comprehension ---")
squares = [x**2 for x in range(5)]
print(squares)

# Dictionary Loop
print("\n--- Dictionary Loop ---")
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")