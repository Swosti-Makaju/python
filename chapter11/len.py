class Vector:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,other):
        return Vector(self.real+other.real,self.imaginary+other.imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}j"  

    def __len__(self):
        return 3

v1=Vector(1,2)
print(v1)