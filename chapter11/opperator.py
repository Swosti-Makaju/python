class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

n=number(1)
m=number(2)

print(n+m)