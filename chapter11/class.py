class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"this is 2d vector with x={self.x} and y={self.y}")

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"this is 3d vector with x={self.x} and y={self.y} and z={self.z}")

a=TwoDVector(1, 2)
a.show()
b=ThreeDVector(1, 2, 3)
b.show()