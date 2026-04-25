numbers=[]
print("Enter 4 numbers")
for i in range(4):
    n=int(input())
    numbers.append(n)
greatest=max(numbers)
print("The greatest number is:", greatest)