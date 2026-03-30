#set stores multiple items in a single variables , written wintin {} .

thisset={"apple","banana","cherry"}
print(thisset) #this prints the set of fruits

thisset={"apple","banana","cherry","apple"}
for x in thisset:
    print(x) #this will print apple only once as set does not allow duplicate items

    thisset.add("orange")
print(thisset) #this adds orange to the set

fruits={"apple","banana","cherry"}
vegetables={"carrot","potato","cabbage"}
food=fruits.union(vegetables)
print(food) #this prints the union of fruits and vegetables

thisset.remove("banana")
print(thisset) #this removes banana from the set

thisset.discard("banana")
print(thisset) #this will not raise an error if banana is not present in the set

#pop() removes a random item from the set
#clear() removes all items from the set
#del() deletes the set completely