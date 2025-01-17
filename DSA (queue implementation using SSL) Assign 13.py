#queue implementation using singly linkedlist
#1. Define a class Queue to implement queue data structure
#using singly linkedlist concept. define __init__() method
#to initialise front and rear reference variable and item_count
#variable to keep track of number of element in the queue.
class Node:
    def __init__(self,item=None, next =None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

#2. define a method is_empty() to check if the queue is empty
#in queue class
    def is_empty(self):
        return self.front == None

#3. in queue class, define enqueue() method to add data into the queue.
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count+=1

#4. in queue class, define dequeue() method to remove front element
#from the queue.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count-=1.

#5. in queue class, define get_front() method to return front element 
#of the queue.
    def get_front(self):
        if self.is_empty():
            raise IndexError("no data in the queue")
        else:
            return self.front.item

#6.in queue class, define get_rear() method to return rear element 
#of the queue.
    def get_rear(self):
        if self.is_empty():
            raise IndexError("no data in the queue")
        else:
            return self.rear.item

#7. In Queue class, define size() method to return size of the queue that is number of
# items present in the queue.
    def size(self):
        if self.is_empty():
            return self.item_count

#driver code:
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())
