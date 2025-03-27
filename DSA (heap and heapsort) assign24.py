#heap and heapsort
#assign 24

#5. Define a class EmptyHeapException to describe custom exception.
class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg
    def __str__(self):
        return self.msg

#1.Define a class Heap to implement Heap data structure with__init__ method
#to create empty heap list.
class Heap:
    def __init__(self):
        self.heap = []

#2.In class Heap, define a method to create heap from a given list of elements.
    def createHeap(self, list1):
        self.heap = []  # Reset heap before creating a new one
        for e in list1:
            self.insert(e)

#3. In class Heap, define a method insert to insert a given element in the heap at
# appropriate position.
    def insert(self, e):
        if e is None:
            raise ValueError("Cannot insert None into heap.")
        self.heap.append(e)
        index = len(self.heap) - 1
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.heap[parentIndex] < self.heap[index]:
                self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
                index = parentIndex
            else:
                break
#4.In class Heap, define a top method which returns the top element of the Heap. Raise
# an exception if Heap is empty.

    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]

#6. In class Heap, define a method delete which deletes the top element and returns it.
# Raise an exception if Heap is empty.
    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        index = 0
        while True:
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2
            maxChildIndex = index

            if leftChildIndex < len(self.heap) and self.heap[leftChildIndex] > self.heap[maxChildIndex]:
                maxChildIndex = leftChildIndex
            if rightChildIndex < len(self.heap) and self.heap[rightChildIndex] > self.heap[maxChildIndex]:
                maxChildIndex = rightChildIndex
            if maxChildIndex == index:
                break
            self.heap[index], self.heap[maxChildIndex] = self.heap[maxChildIndex], self.heap[index]
            index = maxChildIndex
        return max_value


#7.In class Heap, define a method heapSort to sort a given list with the help of Heap.
    def heapSort(self, list1):
        temp_heap = Heap()  # Use a new heap to avoid modifying the existing one
        temp_heap.createHeap(list1)
        sorted_list = []
        while temp_heap.heap:
            sorted_list.insert(0, temp_heap.delete())
        return sorted_list




# Test cases
h = Heap()
list1 = [34, 56, 12, 78, 43, 25, 10, 80, 60]
print("Original list:", list1)

# Testing heap creation
h.createHeap(list1)
print("Heap after creation:", h.heap)

# Testing top element
try:
    print("Top element:", h.top())
except EmptyHeapException as e:
    print(e)

# Testing deletion
print("Deleted element:", h.delete())
print("Heap after deletion:", h.heap)

# Testing insertion
h.insert(90)
print("Heap after inserting 90:", h.heap)

# Testing heap sort
sorted_list = h.heapSort(list1)
print("Sorted list:", sorted_list)

# Testing empty heap exception
empty_heap = Heap()
try:
    empty_heap.delete()
except EmptyHeapException as e:
    print("Exception caught:", e)
try:
    empty_heap.top()
except EmptyHeapException as e:
    print("Exception caught:", e)
