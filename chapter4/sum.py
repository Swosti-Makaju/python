numbers=[]
print("Enter 5 numbers")
for i in range(5):
    n=int(input())
    numbers.append(n)
total=sum(numbers)
print("The sum of the numbers is:", total)