#stack implementation by inheriting list class
#1.define a class Stack to implement stack data structure
#by extending list class.
#stack is child class of list
class Stack(list):
#2. define a method is_empty() to check if the stack is
#empty in Stack class.
    def is_empty(self):
        return len(self)== 0

#3. in stack class, define push() method to add data onto
#the stack
    def push(self,data):
        self.append(data)

#4. In stack class, define pop() method to remove top 
#element from the stack.
#overriding concept if we call pop in stack pop will be there
#and list pop
#infinite recursion if we use pop
    def pop(self):
        if not self.is_empty():
            return super.pop()
        else:
            raise IndexError("stack is empty")

#5.In stack class, defime peek() method to return top 
#element on the stack.
    def peek(self):
        if not self.is_empty():
            return self[-1] #stack object is also called list obj
        else:
            raise IndexError("stack is empty")

#6.In stack class, define size() method  to return size
#of the stack that is number of items present in the stack.
    def size(self):
        len(self)

#7. Implement a way to restrict use of insert() method of
#list class from stack object.
#insert overriding
    def insert(self,index,data):
        raise AttributeError("no attribute 'insert' in stack")

#driver code
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top value=",s1.peek())
print()




