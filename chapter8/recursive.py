def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))


#same function but user should enter the number 
text=input("enter a number: ")
def sum(n):
    if n== 1:
        return 1
    return n + sum(n-1)
print(sum(int(text)))