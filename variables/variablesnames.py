# A variable can have a short name (like x or y or a) or more descriptive name (age, carname, total_output).
# A variable name must start with a letter or underscore character , cannot start with a nuber .
# A variable can only conatin alpha-numeric characters and underscores(A-z,0-9 and _)
# Case sensitive (age,Age and AGE are three different variables)
# Variable name cannot be any of the Python keywords

#example correct way for declaring variable name
myvar="Python"
my_var="Python"
_my_var="Python"
myVar="Python"
MYVAR="Python"
myvar2="Python"  

#exapmle incorrect variable name
# 2myvar="Python"
# my-var="Python"
# my var="Python"

#multi words variables name 
# camel case-each word except first ,starts with a capital letter :
myVariableName="Python"

#pascal case-each word starts with a capital letter :
MyVariableName="Python"

#snake case-each word separated by an underscore :
my_variable_name="Python"

#multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)  #this prints value of x,y,z

x=y=z="🍵"
print(x) #this prints 🍵
print(y) #this prints 🍵
print(z) #this prints 🍵

car = ["Porsche", "BMW", "Thar"]
x, y, z = car
print(x)   #this prints Porsche
print(y)    #this prints BMW
print(z)     #this prints Thar

x="hello"
y="there"
print(x,y) #this prints "hello there" you can also use + operator like print(x+y) for multiple variables

# but for numbers + works as mathematical operator 
x=55
y=99
print(x+y) #this adds the value of x and y but if you try to combine a string and a number with + operator python will give you an error

#  variables created outside of a function are known as global variables.
#  global variables can be used by everyone, both inside and outside of functions
# example
x="Nepal"
def myfunc():
    print(x)
    myfunc()

# creating a variable inside a function , with same name as global variable 
y="Nepal"
def myfunc():
    y="Bhaktapur"
    print(y)
    myfunc

# to create a global variable inside a function, you can use the global keyword 
#if you use global keyword, the variable belongs to global scope :
def myfunc():
    global x
    x="nepal"
    myfunc()
    print(x)

# to change the value of a global variable inside a function , refer to variable by using global keyword
x="wow"
def mnyfunc():
    global x
    x="nice"
    myfunc()
    print(x)

    


