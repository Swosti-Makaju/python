class Programmer:
    company="Microsoft"

    def __init__(self,name,salary,pin):
     self.name=name
     self.salary=salary
     self.pin=pin

p=Programmer("Ramu","100000","1234")
print(p.name,p.salary,p.pin)

r=Programmer("Haggu","100000","1234")
print(r.name,r.salary,r.pin)