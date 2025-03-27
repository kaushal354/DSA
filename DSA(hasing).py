#hashing

#1. simple mod function
def simple_mod_hash(key, size):
    return key % size  # Simple modulo operation

# Example
key = 12345
size = 10
print("Simple Mod Hash:", simple_mod_hash(key, size))

#2. Division method
def division_hash(key, size):
    prime = 7  # Choosing a prime number
    return (key % prime) % size

# Example
print("Division Method Hash:", division_hash(key, size))

#3. Multiplication Method
def multiplication_hash(key, size):
    A = 0.6180339887  # Knuth’s suggested constant
    return int(size * ((key * A) % 1))  # Extract fractional part

# Example
print("Multiplication Method Hash:", multiplication_hash(key, size))

#4. Mid-Square Method
def mid_square_hash(key, size):
    squared_key = key * key
    mid_digits = (squared_key // 100) % 1000  # Extracting the middle digits
    return mid_digits % size

# Example
print("Mid-Square Method Hash:", mid_square_hash(key, size))

#5.Folding Method
def folding_hash(key, size):
    key_str = str(key)
    chunk_size = 2  # Split into chunks of 2 digits
    sum_chunks = sum(int(key_str[i:i+chunk_size]) for i in range(0, len(key_str), chunk_size))
    return sum_chunks % size

# Example
print("Folding Method Hash:", folding_hash(key, size))

#6.Digit Extraction Method
def digit_extraction_hash(key, size):
    key_str = str(key)
    extracted_digits = int(key_str[1] + key_str[3])  # Extracting 2nd and 4th digits
    return extracted_digits % size

# Example
print("Digit Extraction Method Hash:", digit_extraction_hash(key, size))

#7. Binning Method
def binning_hash(key, bin_size):
    return key // bin_size  # Assigns key to a bin

# Example
bin_size = 1000
print("Binning Method Hash:", binning_hash(key, bin_size))


# Method	Use Case
# Simple Mod : Function	Basic hashing, fast but poor distribution
# Division Method :	Works well with prime numbers
# Multiplication Method :	Reduces clustering, good for large datasets
# Mid-Square Method : 	Suitable for small keys, random distribution
# Folding Method :	Works well for large numeric keys
# Digit Extraction :	Useful when specific digits are meaningful
# Binning : 	Groups data efficiently for large key sets

#1. Open Hashing (Separate Chaining)
# Uses linked lists (or lists in Python) to store multiple values in the same bucket when a collision occurs.

# Each index of the hash table contains a list of elements

class OpenHashing:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Each index stores a list

    def hash_function(self, key):
        return key % self.size  # Simple Modulo Hashing

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)  # Append to the list at the index

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]  # Check if key exists in the list

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Example Usage
open_hash = OpenHashing(5)
keys = [10, 20, 15, 25, 30]
for key in keys:
    open_hash.insert(key)

open_hash.display()
print("Search 15:", open_hash.search(15))  # Output: True
print("Search 100:", open_hash.search(100))  # Output: False


#2. 2. Closed Hashing (Open Addressing)
# Instead of using linked lists, it finds an alternative empty slot within the hash table when a collision occurs.

# Techniques include Linear Probing, Quadratic Probing, and Double Hashing

class ClosedHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize an empty hash table

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:  # Linear probing
            index = (index + 1) % self.size  # Move to the next index
        self.table[index] = key

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size
            if index == original_index:  # If we circle back, key not found
                break
        return False

    def display(self):
        print("Hash Table:", self.table)

# Example Usage
closed_hash = ClosedHashing(5)
keys = [10, 20, 15, 25, 30]
for key in keys:
    closed_hash.insert(key)

closed_hash.display()
print("Search 15:", closed_hash.search(15))  # Output: True
print("Search 100:", closed_hash.search(100))  # Output: False


# Key Differences:
# Feature :	Open Hashing (Separate Chaining) :	Closed Hashing (Open Addressing)
# Storage :	Uses linked lists at each index :	Stores all elements in the table itself
# Collision Handling :	Stores multiple elements at one index :	Finds the next available slot
# Search Performance :	Efficient if table is not overloaded :	Slower in worst-case scenarios
# Space Complexity :	Uses extra space for linked lists :	No extra memory needed
# Best When : 	Load factor is high :	Load factor is low
