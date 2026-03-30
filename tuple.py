fruits = ("apple", "banana", "cherry")
print(fruits)  # prints the tuple

print(len(fruits))  # prints number of items
print(type(fruits))  # prints <class 'tuple'>

print(fruits[1])  # prints banana

# one item tuple must have a comma
one_item = ("mango",)
print(one_item)

for item in fruits:
    print(item)  # prints items one by one

numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))  # counts how many times 2 appears
print(numbers.index(3))  # finds the index of 3

# tuples cannot be changed directly, so convert to list first
cars = ("BMW", "Audi", "Tesla")
car_list = list(cars)
car_list[1] = "Toyota"
cars = tuple(car_list)
print(cars)

# joining tuples
a = ("a", "b")
b = ("c", "d")
c = a + b
print(c)
