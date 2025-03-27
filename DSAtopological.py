#DSA topological using dfs:-
def topological_sort_dfs(vertices, adj_list):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Append after visiting all children (Post-order)

    for v in range(vertices):
        if v not in visited:
            dfs(v)

    return stack[::-1]  # Reverse stack to get topological order

# Example Usage
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: []
}
vertices = 5
print("Topological Sort (DFS):", topological_sort_dfs(vertices, graph))
