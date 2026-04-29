

class Employee:
    company="google"
    name="Ramu"
    def show(self):
        print(f"name of employee is {self.name} and company is {self.company}")

class Codeer:
    language="python"
    def printLanguage(self):
        print(f"out of all languages here is ur language: {self.language}")

class Programmer(Employee,Codeer):
    def showLanguage(self):
       print(f"name is {self.company} and is good with {self.language} languaage")

a=Employee()
b=Programmer()

b.show()
b.printLanguage()
b.showLanguage()