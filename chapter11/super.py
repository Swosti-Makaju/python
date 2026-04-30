class animal:
    def __init__(self)->None:
        print("aanimal")
    a=1

class dog(animal):
    def __init__(self)->None:
        print("dog")
    b=2

class babydog(dog):
    def __init__(self)->None:
        super().__init__()
        print("babydog")
    c=3

# o=animal()
# print(o.a)

# o=dog()
# print(o.a,o.b)

o=babydog()
print(o.a,o.b,o.c)