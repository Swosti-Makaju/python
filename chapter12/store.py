num = int(input("Enter a number: "))

with open("Tables.txt", "a") as f:   # use append mode
    f.write(f"\nMultiplication Table of {num}\n")
    f.write("-" * 30 + "\n")
    
    for i in range(1, 11):
        f.write(f"{num} x {i} = {num * i}\n")

print("Table appended to Tables.txt")