class animal:
    def __init__(self)->None:
        print("aanimal")
    a=1

class dog(animal):
    b=2

class babydog(dog):
    c=3

o=animal()
print(o.a)

o=dog()
print(o.a,o.b)

o=babydog()
print(o.a,o.b,o.c)