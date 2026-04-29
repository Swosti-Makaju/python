

from random import randint


class Train:

    def __init__(slf,trainNo):
        slf.trainNo=trainNo

    def book(harr,trainNo,fro,to):
        print(f"your ticket is booked in train no: {harr.trainNo} from {fro} to {to}")
    
    def getStattus(self,trainNo):
        print(f"the status of train no {trainNo} is running on time")
    
    def getFare(self,trainNo,fro,to):
        print(f"the fare from {fro} to {to} is {randint(500,1000)}")

t=Train(12345)
t.book(12345,"Bangalore","Delhi")
t.getStattus(12345)
t.getFare(12345,"Bangalore","Delhi")

#you can change self to any name but it is convention to use self as it is reliable and understanable
#self is a reference to current object and used to acces attributes and methods of classss