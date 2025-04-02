#dynamic programming
#1. Fibonacci Sequence (DP Approach)
#Using Memoization (Top-Down)
def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))  # Output: 55

#Using Tabulation (Bottom-Up)
def fibonacci_tabulation(n):
    if n <= 1:
        return n
    dp = [0, 1]  # Base cases
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(fibonacci_tabulation(10))  # Output: 55



#2.0/1 Knapsack Problem
# Knapsack Solution using DP (Bottom-Up)
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack(weights, values, W))  # Output: 7


#3. Longest Common Subsequence (LCS)
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

X = "AXYT"
Y = "AYZX"
print(lcs(X, Y))  # Output: 2 ("AY")

#4. Coin Change Problem
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 3, 4]
amount = 6
print(coin_change(coins, amount))  # Output: 2

#5.Matrix Chain Multiplication
import sys

def matrix_chain_order(p, i, j, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize
    for k in range(i, j):
        cost = (matrix_chain_order(p, i, k, dp) +
                matrix_chain_order(p, k + 1, j, dp) +
                p[i - 1] * p[k] * p[j])
        dp[i][j] = min(dp[i][j], cost)

    return dp[i][j]

def matrix_chain(p):
    n = len(p)
    dp = [[-1] * n for _ in range(n)]
    return matrix_chain_order(p, 1, n - 1, dp)

p = [1, 2, 3, 4]
print(matrix_chain(p))  # Output: 18


#6. Warshall’s Algorithm (Transitive Closure)
def warshall(graph):
    V = len(graph)
    reach = [[graph[i][j] for j in range(V)] for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach

graph = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
print(warshall(graph))


#7.Floyd’s Algorithm (All-Pairs Shortest Path)
import sys
def floyd_warshall(graph):
    V = len(graph)
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

INF = sys.maxsize
graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
print(floyd_warshall(graph))
