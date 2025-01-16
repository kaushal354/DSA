#queue implementation using list
#1. Define a class Queue to implement queue data structure 
#using list. Define __init__() method to create an empty list
#object as instance object member of queue.

class Queue:
    def __init__(self):
        self.items=[]
        # self.front =None
        # self.rear = None

#2. define a method is_empty() to check if the queue is empty
#in Queue class.
    def is_empty(self):
        return len(self.items) == 0

#3. in Queue class, define enqueue() method to add data at the
#rear end of the queue
    def enqueue(self,data):
        self.items.append(data)

#4. in queue class, define dequeue() method to remove front element
#from the queue.
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("queue underflow")

#5.In a queue class, define get_front() method to return front element
#of the queue.
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("queue underflow")

#6.In a queue class, define get_rear() method to return rear element
#of the queue.
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("queue underflow")

#7.In queue class, define size() method to return size of the queue that is
#number of items present in the queue.
    def size(self):
        return len(self.items)

#driver code:
q1 = Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front:",q1.get_front(),"rear:",q1.get_rear())
try:
    q1.dequeue()
    print("queue has now",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])
