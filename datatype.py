# Data type in python
# In python we have different data types like (text type, numeric type, sequence type, mapping type, set type, boolean type, binary type)
# we can get the data type of any object by using type() function
x="hello"
print(type(x)) #this prints <class 'str'> which means x is a string data type

y=55
print(type(y)) #this prints <class 'int'> which means y is an integer data type

z=55.99
print(type(z)) #this prints <class 'float'> which means z is a float data type

a=1j
print(type(a)) #this prints <class 'complex'> which means a is a complex data type

b=["apple","banana","cherry"]
print(type(b)) #this prints <class 'list'> which means b is a list data type
# list is a collection which is ordered and changeable. Allows duplicate members

c=("apple","banana","cherry")
print(type(c)) #this prints <class 'tuple'> which means c is a tuple data type
# tuple is a collection which is ordered and unchangeable. Allows duplicate members

d=range(6)
print(type(d)) #this prints <class 'range'> which means d is a range data type
# range is a collection which is ordered and unchangeable. Allows duplicate members

e={"name":"john","age":36}
print(type(e)) #this prints <class 'dict'> which means e is a dictionary data type
# dictionary is a collection which is unordered, changeable and indexed. No duplicate members   

f={"apple","banana","cherry"}
print(type(f)) #this prints <class 'set'> which means f is a set data type
# set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members

g=frozenset({"apple","banana","cherry"})
print(type(g)) #this prints <class 'frozenset'> which means g is a frozenset data type
# frozenset is a collection which is unordered and unindexed. No duplicate members

h=True
print(type(h)) #this prints <class 'bool'> which means h is a boolean data type
# boolean represents one of two values: True or False

i=b"hello"
print(type(i)) #this prints <class 'bytes'> which means i is a bytes data type
# bytes is a collection of data which is ordered and unchangeable. Allows duplicate members 

j=bytearray(5)
print(type(j)) #this prints <class 'bytearray'> which means j is a bytearray data type
# bytearray is a collection of data which is ordered and changeable. Allows duplicate members

k=memoryview(bytes(5))
print(type(k)) #this prints <class 'memoryview'> which means k is a memory  view data type
# memoryview is a memory view object which is a safe way to expose the buffer protocol in Python

# A variable is a container for a value, which can be of any data type
# In Python, you do not need to declare a variable with any particular type and it can even change type after it has been set
# A variable is created the moment you first assign a value to it
x = 5
y = "Hello, World!"
print(x)
print(y) #this prints value of x and y

# you can also assign multiple values to multiple variables in one line
# examples
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)  #this prints value of a,b,c   
# note : the number of variables must be equal to the number of values, otherwise you will get an error

# you can assign the same value to multiple variables in one line
x = y = z = "🍵"
print(x) #this prints 🍵
print(y) #this prints 🍵
print(z) #this prints 🍵

# unpacking a collection
fruits = ["Apple", "Banana", "Cherry"]  
x, y, z = fruits
print(x)   #this prints Apple
print(y)    #this prints Banana
print(z)     #this prints Cherry

