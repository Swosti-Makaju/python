class Demo:
    a=6

o=Demo()
print(o.a) #prints class attribute cause instance attribute is not present
o.a=0   #instance attribute set
print(o.a) #prints instance attribute as it is present
print(Demo.a) #prints class attribute