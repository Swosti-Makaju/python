from functools import reduce

l=[6554,4666,6458,546,5468,65444453]

def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
print(reduce(greater, l))