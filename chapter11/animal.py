class animal:
    def __init__(self)->None:
        print("aanimal")
    a=1

class dog(animal):
    @staticmethod
    def bark():
        print("woof")
    b=2

class babydog(dog):
    c=3

b=dog()
b.bark()
# o=animal()
# print(o.a)

# o=dog()
# print(o.a,o.b)

# o=babydog()
# print(o.a,o.b,o.c)