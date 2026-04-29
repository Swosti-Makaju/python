class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is {self.n*self.n}") 

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}") 

    def squareroot(self):
        print(f"the square root is {self.n**0.5}") 

a=Calculator(5)
a.square()
a.cube()
a.squareroot()  