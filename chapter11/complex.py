class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,other):
        return Complex(self.real+other.real,self.imaginary+other.imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}j"    

c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)