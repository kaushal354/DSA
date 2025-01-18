#priority queue implementation using list

# 1.Define a class to implement priority queue data structure using list.
# Provide __init__() method to create a list object (initially empty).

class priorityQueue:
    def __init__(self):
        self.items = []

#2.define a push method in PriorityQueue class to insert new data with given priority.
    def push(self,data,priority):
        index = 0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))

#3.Define is_empty method in PriorityQueue class to check if the priority queue is empty
    def is_empty(self):
        return len(self.items)==0

#4.Define a pop method in PriorityQueue class, which returns the highest priority data
# stored in the priority queue data structure. Raise exception if priority queue is empty.

    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")
        return self.items.pop(0)[0]

# 5.In class PriorityQueue. define a method size return the number Of elements
# present in the priority queue.

    def size(self):
        return len(self.items)

#driver code:
p = priorityQueue()
p.push("Amit",4)
p.push("Arjun",7)
p.push("Ashima",2)
p.push("Agrah",5)
p.push("Anant",8)
p.push("Ambika",1)

while not p.is_empty():
    print(p.pop())

