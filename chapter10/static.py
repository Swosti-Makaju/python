class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is {self.n*self.n}") 

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}") 

    def squareroot(self):
        print(f"the square root is {self.n**0.5}") 

    @staticmethod
    def greet():
        print("Welcome to the calculator program")    

a=Calculator(5)
a.greet() #static method called using object
a.square()
a.cube()
a.squareroot()  