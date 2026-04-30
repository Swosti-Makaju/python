class food:
    a=1
    @classmethod
    def show(cls):
        print(f"this is class method and value of a is {cls.a}")
f=food()
f.a=55
f.show()