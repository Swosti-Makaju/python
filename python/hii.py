my_list=[1, 5 ,8 ,6 ,9 ,88]
my_list[2]

my_list=[[1, 5 ,8 ,6 ],[9 ,88],"swosti"]
my_list[2][1]

num =int( input("......"))
num

for i in range(0,3):
      print("hello")

      sentence ="i am a student"
      sentence.split()

      list=["apple","ball","tt"]
      list[1]="dough"
      list

      list=["apple","ball","tt",5,8]
      list[1:3]=["dough",7,6,2]
      list

list=["apple","ball","tt"]
list.remove("apple")


list=["apple","ball","tt"]
list.pop()

list=["apple","ball","tt"]
del list[0]

list=["apple","ball","tt"]
list.clear()

cars=("hehehe","huhuhu","hahaha")
cars
cars[1:3]

cars=("car",)
cars

set1={1,2,3,True,"hi"}
set1.add(4)
print(set1)

set1={1,2,3,1,"hi"}
print(set1)

set1={1,2,3,1,"hi"}
set2={11,22,3,13,"hi"}
print(set1|set2)

set1={1,2,3,1,"hi"}
set2={11,22,3,13,"hi"}
print(set1&set2)

array = [12, 34, 55, 32, 54]
for i in range(0, len(array)):
    print(array[i], end=" ")

array.append(99)
array[0] = 100
print("\narray after modify:")
for i in range(0, len(array)):
    print(array[i], end=" ")

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(a)
print(b)
np.size(a)
np.shape(b)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
a[1, 1]
a[:,1]

import pandas as pd
df=pd.read_csv("data/survey_results_public.csv")