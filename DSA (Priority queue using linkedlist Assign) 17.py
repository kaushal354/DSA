#priority queue using linkedlist

#1.Define a Node class with instance member variables item, priority and next.
class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

# 2.Define a class PriorityQueue to implement priority queue data structure using singly
# linked list. Provide __init__() method to create a start reference variable (initially
# containing None) and item count variable (initially O).
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0

#3.Define is_empty method in PriorityQueue class to check if the priority queue is empty.
    def is_empty(self):
        return self.start==None

# 4.Define a push method in PriorityOueue class to insert new data with given priority.
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority <self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1





# 5.Define a pop method in PriorityQueue class. which returns the highest priority data
# stored in the priority queue data structure. Raise exception if priority queue is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data



#6.In class PriorityQueue, define a method size to return the number of elements
# present in the priority queue.
    def size(self):
        return self.item_count

#driver code:
p=PriorityQueue()
p.push("Amit",4)
p.push("Arjun",7)
p.push("Ashima",2)
p.push("Agrah",5)
p.push("Anant",8)
p.push("Ambika",1)

while not p.is_empty():
    print(p.pop())

