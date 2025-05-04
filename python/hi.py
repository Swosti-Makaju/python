colors=["blue", "black"]
for i in colors:
    print(i)

i=1
while i<6:
    print(i)
    i+=2

x=0
while not(1<= x<=200):
    x= int(input("Please enter the value between 1 to 200: "))
    print("valid no", x)

    for i in range (4):
        x= int(input("Please enter the value between 50 aand 100: "))
        if 50<=x<=100:
            print("valid no", x)
            break
        else:
            print("Inalid number, try again: ")

       