#deque using linkedlist concept
#1.Define a class Node with instance object member variables prev, item and next.
class Node:
    def __init__(self,item=None,prev = None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

#2.Define a class Deque to implement deque data structure using doubly linked list
# concept. Define __init__() method to initialise front and rear reference variable; and
# item_count variable to keep track of number of elements in the deque.
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count=0

#3.Define a method is_empty() to check if the deque is empty in Deque class.
    def is_empty(self):
        return self.item_count==0

#4.In Deque class. define insert_front() method to add data at front of the deque.
    def insert_front(self,data):
        n = Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n

        self.front =n
        self.item_count+=1

#5.In Deque class, define insert_rear() method to add data at the rear of the deque.
    def insert_rear(self,data):
        n = Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear =n
        self.item_count+=1

#6. In Deque class, define delete_front() to remove front element from the deque.
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count-=1

#7.In Deque class, define delete_rear() to remove rear element from the deque.
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count-=1

# 8.In Deque class, define get_front() method to return front element of the deque.
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.item



# 9.In Deque class, define get_rear() method to return rear element of the deque.
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.item

#10.In Deque class, define size() method to return size of the deque that is number of
# items present in the deque.
    def size(self):
        return self.item_count

#driver code:
d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(),d1.get_rear())
