#backtracking
# 1.Example 1: N-Queens Problem
def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, N):
                return True
            board[i][col] = 0  # **Backtrack**
    return False

N = 4  # Change for N-Queens
board = [[0] * N for _ in range(N)]
solve_n_queens(board, 0, N)
for row in board:
    print(row)


#2.Example 2: Subset Sum Problem
def subset_sum(arr, index, target, path):
    if target == 0:
        print(path)
        return
    if index >= len(arr) or target < 0:
        return
    subset_sum(arr, index + 1, target - arr[index], path + [arr[index]])  # Include
    subset_sum(arr, index + 1, target, path)  # Exclude

arr = [3, 34, 4, 12, 5, 2]
target = 9
subset_sum(arr, 0, target, [])


#3.Travelling Salesman Problem (TSP) using Backtracking
import sys

def tsp(graph, visited, curr_pos, n, count, cost, min_cost):
    if count == n and graph[curr_pos][0]:
        min_cost[0] = min(min_cost[0], cost + graph[curr_pos][0])
        return
    
    for i in range(n):
        if not visited[i] and graph[curr_pos][i]:
            visited[i] = True
            tsp(graph, visited, i, n, count + 1, cost + graph[curr_pos][i], min_cost)
            visited[i] = False  # **Backtrack**

def solve_tsp(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True  # Start from city 0
    min_cost = [sys.maxsize]
    
    tsp(graph, visited, 0, n, 1, 0, min_cost)
    return min_cost[0]

graph = [[0, 10, 15, 20], 
         [10, 0, 35, 25], 
         [15, 35, 0, 30], 
         [20, 25, 30, 0]]

print("Minimum cost of TSP:", solve_tsp(graph))


