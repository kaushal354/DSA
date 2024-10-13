#DSA (ARRAY) ASSIGNMENT 1
#1. given an array with some integer type values. write a python script to sort array values?
import numpy as np
A = np.array([5,2,27,18,15])
A.sort()
print(A)
print(type(A))

#2.Given a list of heterogenous elements. write a python
#script to remove all the non int values from the list.
b = [1,"hello",3,"i",5,"airtel",3.6]
c = []
for i in b:
    if isinstance(i,int):
        c.append(i)

print(c)

#3. write a python script to calculate average of elements of a list.
#1.method
import numpy as np
list2 = [1,2,3,4,5,6]
avg = np.mean(list2)
print(avg)
#2.method
list3 = [1,2,3,4,5,6]
a = 0
for i in list3:
    a = i + a
print(a)
a = a / len(list3)
print(a)

#4. write a python script to create a list of first n prime number:
num = int(input("enter n number:"))
primeno = []
b = 0
for i in range(1,num):
    for j in range(1,i+1):
        if i % j == 0:
            b = b + 1
        else:
            b = b + 0
    if b == 2:
        primeno.append(i)
    b = 0
print(primeno)

#5. write a python scirpt to create a list of first n
#terms of fibonacci series
num = int(input("enter a n terms"))
x = []
a = 0
x.append(a)
b = 1
x.append(b)
for i in range(0,num-2):
    if a < b:
        a = a + b
        x.append(a)
    else:
        b = b + a
        x.append(b)
print(x)








