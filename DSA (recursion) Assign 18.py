#SIMPLE PROBLEM ON RECURSION

# 1.write a recursive function to print N natural numbers in reverse order.
def funrev(n):
    if n>0:
        print(n,end=" ")
        funrev(n-1)

funrev(10)

print("\n")
#2.write a recursive function to print N natural numbers
def fun(n):
    if n>0:
        fun(n-1)
        print(n,end=" ")
fun(10)

print("\n")

#3.Write a recursive function to print first N odd natural numbers.
def fun(n):
    if n>0:
        fun(n-1)
        if n %2 != 0:
            print(n,end=" ")
fun(10)

print("\n")

#4.Write a recursive function to print first N even natural numbers.
def fun(n):
    if n>0:
        fun(n-1)
        if n %2 == 0:
            print(n,end=" ")
fun(10)

print("\n")
#5.write a recursive function to print first N odd natural numbers in reverse order.
def funrev(n):
    if n>0:
        if n%2 != 0:
            print(n,end=" ")
        funrev(n-1)

funrev(10)

print("\n")
#6. Write a recursive function to print first N even natural numbers in reverse order.

def funrev(n):
    if n>0:
        if n%2 == 0:
            print(n,end=" ")
        funrev(n-1)

funrev(10)