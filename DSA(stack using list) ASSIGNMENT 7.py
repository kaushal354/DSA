#stack using list
#1. define a class stack to implement stack data structure
#using list. define __init__() method to create an empty
#list object as instance object member of stack.

class stack:
    def __init__(self):
        self.items = []

#2. define a method is_empty() to check if the stack is
#empty in stack class.

    def is_empty(self):
        return len(self.items) == 0

#3. in stack class, define push() method to add data
#onto the stack.
    def push(self,data):
        self.items.append(data)

#4. in stack class, define pop() method to remove top
#element from the stack.

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")

#5. in stack class, define peek() method to return top
#element on the stack.

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("stack is empty")

#6. In stack class, define size() method to return size
#of the stack that is number of items present in the 
#stack.

    def size(self):
        return len(self.items)

#driver code
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is ",s1.peek())
print("Removed element is",s1.pop())
print("Top element is ",s1.peek())
print("size =", s1.size())
print()

