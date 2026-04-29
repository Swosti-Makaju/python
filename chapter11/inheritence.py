class Employee:
    company="google"
    name="Ramu"
    salary=100000
    def show(self):
        print(f"name of employee is {self.name} and salary is {self.salary}")

# class Programmer(Employee):
#     company="microsoft"
#     def show(self):
#         print(f"name is {self.name} and salary is {self.salary} and company is {self.company}")

#     def showLanguage(self):
#         print(f"name is {self.name} and is good with {self.language} languaage")

class Programmer(Employee):
    company="microsoft"
    def showLanguage(self):
       print(f"name is {self.name} and is good with {self.language} languaage")

a=Employee()
b=Programmer()

b.show()

print(a.company,b.company) 