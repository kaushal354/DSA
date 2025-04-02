#greedy algo
#1. prism algorithm(minimum spanning tree)
import heapq
def prim(graph):
    n = len(graph)  # Number of nodes
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node), starting from node 0
    mst_cost = 0
    mst_edges = []

    while len(mst_edges) < n - 1:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:  # Skip already visited nodes
            continue

        visited[u] = True
        mst_cost += weight

        for v, w in graph[u]:
            if not visited[v]:  # Add only unvisited nodes
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))  # Store MST edges

    return mst_cost, mst_edges

# Example Graph (Adjacency List)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

mst_cost, mst_edges = prim(graph)
print("Minimum Spanning Tree Cost:", mst_cost)
print("Edges in MST:", mst_edges)


#2. Krushkal's algorithm(minimum spanning tree)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Used for union by rank

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False  # Cycle detected

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    dsu = DisjointSet(n)
    mst = []
    mst_cost = 0

    for u, v, weight in edges:
        if dsu.union(u, v):  # If the edge doesn't form a cycle, include it
            mst.append((u, v, weight))
            mst_cost += weight

        if len(mst) == n - 1:  # Stop when MST has (V-1) edges
            break

    return mst_cost, mst

# Example Usage
edges = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]
n = 4  # Number of vertices

mst_cost, mst_edges = kruskal(n, edges)
print("Minimum Spanning Tree Cost:", mst_cost)
print("Edges in MST:", mst_edges)


#3. Activity Selection Problem (Greedy Algorithm)
# The Activity Selection Problem is a Greedy Algorithm that selects
# the maximum number of non-overlapping activities based on their start and end times.
# Algorithm Steps:
# 1.Sort activities by their end time.
# 2.Pick the first activity (since it has the earliest end time).
# 3.For each next activity, select it only if it starts after the last selected activity ends.
# 4.Repeat until all activities are checked.

def activity_selection(activities):
    # Sort activities based on end time
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_end_time = -1

    for start, end in activities:
        if start >= last_end_time:  # Select if it doesn't overlap
            selected_activities.append((start, end))
            last_end_time = end  # Update last end time

    return selected_activities

# Example Usage
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 10), (5, 7)]
selected = activity_selection(activities)

print("Selected Activities:", selected)


#4. Dijkstra’s Algorithm (Shortest Path Algorithm)
import heapq

def dijkstra(graph, start):
    # Number of vertices
    n = len(graph)

    # Distance array (initialize all distances as infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to source is 0

    # Priority queue (min-heap) to get the node with the smallest distance
    pq = [(0, start)]  # (distance, node)

    while pq:
        curr_distance, node = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if curr_distance > distances[node]:
            continue

        # Relaxation step
        for neighbor, weight in graph[node].items():
            distance = curr_distance + weight

            # If a shorter path is found, update and push to priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example Graph (Adjacency List Representation)
graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 1, 'B': 2, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Output shortest paths from source
print("Shortest distances from node", start_node)
for node, distance in shortest_paths.items():
    print(f"To {node}: {distance}")


#5.Fractional Knapsack Problem (Greedy Algorithm)

def fractional_knapsack(items, capacity):
    # Sort items based on value/weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0  # Total value of the knapsack
    knapsack_contents = []  # Store selected items

    for name, value, weight in items:
        if capacity >= weight:
            # Take the full item
            knapsack_contents.append((name, weight, value))
            total_value += value
            capacity -= weight
        else:
            # Take a fraction of the item
            fraction = capacity / weight
            knapsack_contents.append((name, capacity, value * fraction))
            total_value += value * fraction
            break  # Knapsack is full

    return total_value, knapsack_contents

# Example Usage
items = [
    ("Item 1", 60, 10),  # (name, value, weight)
    ("Item 2", 100, 20),
    ("Item 3", 120, 30)
]
capacity = 50

max_value, selected_items = fractional_knapsack(items, capacity)

print("Maximum Value:", max_value)
print("Selected Items:")
for item in selected_items:
    print(item)


#6.huffman coding (Data Compression) – Greedy Algorithm
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Overriding < operator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)  # Create min-heap

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)

    return heap[0]  # Root of Huffman Tree

def generate_huffman_codes(node, prefix="", codes={}):
    if node:
        if node.char:  # Leaf node
            codes[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codes)
        generate_huffman_codes(node.right, prefix + "1", codes)
    return codes

def huffman_encoding(text):
    if not text:
        return "", {}

    # Step 1: Calculate frequency of characters
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Build Huffman Tree
    root = build_huffman_tree(frequency)

    # Step 3: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(root)

    # Step 4: Encode the text
    encoded_text = "".join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes

# Example Usage
text = "huffman coding example"
encoded_text, codes = huffman_encoding(text)

print("Huffman Codes:", codes)
print("Encoded Text:", encoded_text)

