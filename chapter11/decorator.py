class food:
    a=1

    @classmethod
    def show(cls):
        print(f"this is class method and value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

f=food()
f.a=55

f.name="Apple Appleu"
print(f.name)


f.show()