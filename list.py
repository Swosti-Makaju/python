fruits=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(fruits)  #this prints the list of fruits

print(len(fruits)) #this prints the number of items in the list

print(type(fruits)) #this prints <class 'list'> which means fruits is a list data type
# list is a collection which is ordered and changeable. Allows duplicate members

print(fruits[3]) #prints orange which is indexed at 3 as list are started from index o

list=["car","bike","bus","train","aeroplane"]
list[1]="cycle" #changing the value at index 1 from bike to cycle
print(list) 

if "car" in list:
    print("yes, 'car' is in the list")

for x in list:
    print(x)  #this prints all the items in the list one by one

    list[1:3]=["scooter","truck"] #changing the value at index 1 and 2
print(list)

letters=["a","b","c","d","e","f","g","h","i","j","k"]
letters.append("z")
print(letters) #adds 'z' at end of list

for x in letters:
    print(x)  #this prints all the items in the list one by one 

letters.insert(1,"x")
print(letters) #adds 'x' at index 1

letters.remove("d")
print(letters) #removes 'd'

letters.pop()
print(letters) #removes last item

letters.pop(5)
print(letters) #removes item at index 5

del letters[0]
print(letters) #removes item at index 0

letters.clear()
print(letters) #removes all items from the list

for x in letters:
    print(x)  #this will not print anything as the list is cleared

for i in range(5):
    letters.append(i)
print(letters) #this prints [0, 1, 2, 3, 4]

z=["p","q","r","s"]
i=0
while i<len(z):
    print(z[i])
    i=i+1 #outputs p q r s one by one

z=["p","q","r","s"]
i=0
while i<len(z):
    print(z[2])  #print r multiple times 
    i=i+1

    [print(x) for x in z] #prints items one by one 

    a=["1","2","3","4","5"]
    b=["6","7","8","9","10"]
    a+=b
    print(a)

#using append
a=['a','b']
b=['s','t']
for x in b:
    a.append(b)
    a.extend(b)
    print(a)

numbers=[5,2,9,1,7]
numbers.sort()
print(numbers) #sorts the list in ascending order

numbers.reverse()
print(numbers) #reverses the order of the list