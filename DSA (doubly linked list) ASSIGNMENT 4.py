#doubly linked list

#1. define a class Node to describe a node of a doubly linkedlist.

class Node:
    def __init__(self,prev = None,item = None,next = None):
        self.prev = prev
        self.item = item
        self.next = next

#2. define a class DLL to implement doubly linkedlist with __init__()
# method to create and initialise start reference variable.

class DLL:
    def __init__(self,start = None):
        self.start = start

#3. define a method is_empty() to check if the linkedlist is empty
#DLL class

    def is_empty(self):
        return self.start == None

#4. In class DLL, define a method insert_at_start() to insert an element
#at the starting of the list.
    def insert_at_start(self,data):
        n = Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

#5.In class DLL, define a method insert_at_last() to insert an element at the end of the
#list.
    def insert_at_last(self,data):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next
        n = Node(temp,data,None)
        if temp == None:
            self.start = n
        else:
            temp.next = n

#6. In class DLL, define a method search() to find the node with specified element value.
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

# 7.In class DLL, define a method insert_after() to insert a new node after a given node
# of the list.
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

#8. In class DLL. define a method to print all the elements of the list.
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next

#9.In class DLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

#10. In class DLL, define a method delete_last() to delete first element from the list.
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start =None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

#11. in class Dll, define a method to delete_item() to delete specific element from the list.
    def delete_item(self,data):
       if self.start is None:
            pass
       else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

#12. in class Dll, implement iterator for dll to access all the elements of the list in a sequence.
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


#driver code
my_list = DLL()
my_list.insert_at_start(10)
my_list.insert_at_last(20)
my_list.insert_after(my_list.search(10),15)
for x in my_list:
    print(x,end=" ")
my_list.delete_first()
print("\n")
for x in my_list:
    print(x,end=" ")
