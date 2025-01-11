#1. import module containing singly linked list code in your
#python file.
from assign3m import *
#2. define a class stack to implement stack datastructure
#define __init__() method to create singly linkedlist(SLL)
#object
class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count = 0

#3. Define a method is_empty() to check if the stack
#is empty in stack class.
    def is_empty(self):
        return self.mylist.is_empty()

#4.IN stack class, define push() method to add data onto the stack.
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1

#5.in stack class, define a pop() method to remove top element from 
#the stack.
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
        else:
            raise IndexError("stack is empty")

#6.in stack class, define peek() method to return 
#top element on the stack.
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item

#7. In stack class, define size() method to return size
# of the stack that is number of items present in the stack.
    def size(self):
        return self.item_count

#driver code
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is",s.peek())
s.pop()
print("Top element is",s.peek())

