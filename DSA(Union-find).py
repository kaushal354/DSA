#union and find operation using python
# This implementation includes:
# Find with Path Compression: Makes future lookups faster.
# Union by Rank: Ensures the tree remains balanced.
# Connected: Checks if two elements belong to the same set.
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]  # Parent array
        self.rank = [1] * size  # Rank array to keep tree balanced
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Example Usage
uf = UnionFind(10)  # Create a Union-Find with 10 elements
uf.union(1, 2)
uf.union(2, 3)
print(uf.connected(1, 3))  # True
print(uf.connected(1, 4))  # False
