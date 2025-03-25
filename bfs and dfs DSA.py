# Depth-First Search (DFS) - Recursive
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)  # Using list instead of set
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Depth-First Search (DFS) - Iterative
def dfs_iterative(graph, start):
    visited = []  # Using list instead of set
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            stack.extend(graph[node][::-1])  # Reverse to maintain order

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = []  # Using list instead of set
    queue = [start]

    while queue:
        node = queue.pop(0)  # Using list as a queue
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

print("DFS Recursive:")
dfs_recursive(graph, 'A', [])
print("\nDFS Iterative:")
dfs_iterative(graph, 'A')
print("\nBFS:")
bfs(graph, 'A')

