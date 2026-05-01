try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Infinite (division by zero is not allowed)")