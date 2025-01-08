#circular doubly linkedlist
#1. Define a class Node to describe a node of a circular doubly linkedlist.
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

#2.define a class CDLL, to implement circular doubly linkedlist with __init__() method to create
#and initialize start reference variable.
class CDLL:
    def __init__(self,start=None):
        self.start = start

#3. define method is_empty() to check if the linked list is empty in CDLL class.
    def is_empty(self):
        return self.start==None

#4. in class CDLL, define a method insert_at_start() to insert an element at the starting
#of the list.
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n

#5. in class CDLL, define a method insert_at_last() to insert an element
#at the end of the list.
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n

#6.in class CDLL, define a method search() to find the node with specified
#element value.
    def search(self,data):
        temp = self.start
        if temp==None:
            return None
        if temp.item ==data:
            return temp
        else:
            temp=temp.next

        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None

#7.In class CDLL, define a method insert_after() to insert a new node after
#a given node of the list.
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

#8.In class CDLL, define a method to print all the element of the list.
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item,end=" ")
                temp=temp.next

#9.in class CDLL, define a method delete_first() to delete first element
#from the list.
    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start =None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start=self.start.next

#10. in class CDLL, define a method delete_last() to delete last element
#from the list.
    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start =None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

#11. in class CDLL, define a method delete_item() to delete specified element 
#from the list.
    def delete_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item == data:
                self.delete_first()
        else:
            temp=temp.next
            while temp is not self.start:
                if temp.item==data:
                    temp.next.prev= temp.prev
                    temp.prev.next = temp.next

#12.in class CDLL, implement iterator for CDLL to access all the elements
#for the list in a sequence.
    def __iter__(self):
        return CDLLIterator(self.start)
class CDLLIterator:
    def __init__(self,start):
        self.current =start
        self.start = start
        self.count = 0 
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current = self.current.next
        return data

#driver code
mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30),35)

for x in mylist:
    print(x,end=" ")

print()