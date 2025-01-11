#stack implementation by extend singly linkedlist
#1. import module contating singly linkedlist code
#in your python file.
from assign3m import *

#2.Define a class Stack to implement stack data
#structure by inheriting SLL class.
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0

#3.define a method is_empty() to check if the stack
#is empty in stack class.
    def is_empty(self):
        return super().is_empty()

#4. In stack class, define push() method to add data
#onto the stack.
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

#5. In stack class, define pop() method to remove top
#element from the stack.
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("stack underflow")

#6. In stack class, define peek() method to return top
#element on the stack.
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("stack underflow")

#7. in stack class, define size() method to return size
#of the stack that is number of items present in the stack.
    def size(self):
        return self.item_count

#driver code
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top element on the stack:",s1.peek())
s1.pop()
print("top element on the stack:",s1.peek())