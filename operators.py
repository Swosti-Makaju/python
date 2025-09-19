# python operators are special symbols that perform specific operations on one or more operands
# we have different types of operators in python like (arithmetic, assignment, comparison, logical, bitwise, membership, identity)
# we can use these operators to perform various operations on data

# Arithmetic operators
a = 10
b = 5
print(a + b)  #this prints 15
print(a - b)  #this prints 5
print(a * b)  #this prints 50
print(a / b)  #this prints 2.0
print(a % b)  #this prints 0
print(a ** b) #this prints 100000
print(a // b) #this prints 2

# Assignment operators
x = 10
x += 5  #this is equivalent to x = x + 5
print(x)  #this prints 15
x -= 3  #this is equivalent to x = x - 3
print(x)  #this prints 12
x *= 2  #this is equivalent to x = x * 2
print(x)  #this prints 24
x /= 4  #this is equivalent to x = x / 4
print(x)  #this prints 6.0
x %= 4  #this is equivalent to x = x % 4
print(x)  #this prints 2.0
x **= 3  #this is equivalent to x = x ** 3
print(x)  #this prints 8.0
x //= 2  #this is equivalent to x = x // 2
print(x)  #this prints 4.0

# Comparison operators
p = 10  
q = 5
print(p == q)  #this prints False
print(p != q)  #this prints True
print(p > q)   #this prints True    
print(p < q)   #this prints False
print(p >= q)  #this prints True    
print(p <= q)  #this prints False

# Logical operators
m = True
n = False
print(m and n)  #this prints False
print(m or n)   #this prints True
print(not m)    #this prints False
print(not n)    #this prints True

# Bitwise operators
c = 10  #binary: 1010
d = 4   #binary: 0100
print(c & d)  #this prints 0 (binary: 0000)
print(c | d)  #this prints 14 (binary: 1110)
print(c ^ d)  #this prints 14 (binary: 1110)
print(~c)     #this prints -11 (binary: ...11110101)
print(c << 2) #this prints 40 (binary: 101000)
print(c >> 2) #this prints 2 (binary: 0010) 

# Membership operators
list1 = [1, 2, 3, 4, 5] 
print(3 in list1)    #this prints True
print(6 not in list1) #this prints True
print(2 in list1)    #this prints True
print(7 not in list1) #this prints True     
print(10 in list1)   #this prints False
print(1 not in list1) #this prints False

# Identity operators
a = 10  
b = 10
c = 5
print(a is b)  #this prints True because both a and b point to the same object
print(a is not c) #this prints True because a and c point to different objects  
print(a is c)  #this prints False because a and c point to different objects
print(b is not c) #this prints True because b and c point to different objects
print(a is not b) #this prints False because both a and b point to the same object
print(c is not a) #this prints True because c and a point to different objects
print(c is not b) #this prints True because c and b point to different objects

# operator precedence
# operator precedence determines the order in which operators are evaluated in an expression
x = 10 + 5 * 2  #multiplication has higher precedence than addition
print(x)  #this prints 20

y = (10 + 5) * 2  #parentheses have highest precedence
print(y)  #this prints 30

z = 10 / 2 + 3 * 2 - 1  #division, multiplication, addition, and subtraction
print(z)  #this prints 10.0

w = 10 // 3 + 2 ** 3 * 2  #floor division, exponentiation, multiplication, and addition
print(w)  #this prints 18.0

a = 5 + 3 > 2 and 4 < 6  #comparison and logical operators
print(a)  #this prints True

b = not (5 + 3 > 2) or 4 < 6  #comparison and logical operators with parentheses
print(b)  #this prints True

