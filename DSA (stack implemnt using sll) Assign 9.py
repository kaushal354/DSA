#stack implementation using singly linkedlist

#1. define a class stack data structure using linked list concept, Define
#__init__() method to initialise start reference variable and item_count
#variable to keep track of number of elements in the stack.

class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

#2. define a method is_empty() to check if the stack is empty in Stack
#class.
    def is_empty(self):
        return self.start == None

#3.in Stack class, define push() method to add data onto the stack.
    def push(self,data):
        n = Node(data,self.start)
        self.start = n
        self.item_count+=1

#4.in stack class, define pop() method to remove top element from the stack.
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("stack is empty(underflow)")

#5. In stack class, define peek() method to return top element on the stack.
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()

#6.In stack class, define size() method to return size of the stack that is
#number of items preset in the stack.
    def size(self):
        return self.item_count


s1= Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Total element in the stack=",s1.size())
print("top element on the stack is",s1.peek())
print("Popped element is",s1.pop())
print("Total element in the stack=",s1.size())
print("top element on the stack is",s1.peek())