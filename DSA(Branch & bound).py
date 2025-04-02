#branch & bound
#1.Example: Travelling Salesman Problem (TSP) using Branch and Bound
import sys

class TSPBranchBound:
    def __init__(self, graph):
        self.n = len(graph)
        self.graph = graph
        self.final_res = sys.maxsize
        self.final_path = []
        
    def copy_to_final(self, curr_path):
        self.final_path = curr_path[:]
        self.final_path.append(curr_path[0])
        
    def first_min(self, i):
        return min([self.graph[i][j] for j in range(self.n) if i != j])
    
    def second_min(self, i):
        first, second = sys.maxsize, sys.maxsize
        for j in range(self.n):
            if i != j:
                if self.graph[i][j] <= first:
                    second = first
                    first = self.graph[i][j]
                elif self.graph[i][j] < second:
                    second = self.graph[i][j]
        return second
    
    def tsp_recursive(self, curr_bound, curr_weight, level, curr_path, visited):
        if level == self.n:
            if self.graph[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.graph[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.final_res:
                    self.copy_to_final(curr_path)
                    self.final_res = curr_res
            return
        
        for i in range(self.n):
            if (self.graph[curr_path[level-1]][i] != 0 and not visited[i]):
                temp_bound = curr_bound
                curr_weight += self.graph[curr_path[level-1]][i]
                if level == 1:
                    curr_bound -= (self.first_min(curr_path[level-1]) + self.first_min(i)) / 2
                else:
                    curr_bound -= (self.second_min(curr_path[level-1]) + self.first_min(i)) / 2
                
                if curr_bound + curr_weight < self.final_res:
                    curr_path[level] = i
                    visited[i] = True
                    self.tsp_recursive(curr_bound, curr_weight, level + 1, curr_path, visited)
                
                curr_weight -= self.graph[curr_path[level-1]][i]
                curr_bound = temp_bound
                visited[i] = False

    def solve_tsp(self):
        curr_bound = 0
        curr_path = [-1] * (self.n + 1)
        visited = [False] * self.n
        for i in range(self.n):
            curr_bound += (self.first_min(i) + self.second_min(i))
        curr_bound = curr_bound // 2
        
        visited[0] = True
        curr_path[0] = 0
        
        self.tsp_recursive(curr_bound, 0, 1, curr_path, visited)
        return self.final_res, self.final_path

graph = [[0, 10, 15, 20], 
         [10, 0, 35, 25], 
         [15, 35, 0, 30], 
         [20, 25, 30, 0]]

tsp_solver = TSPBranchBound(graph)
cost, path = tsp_solver.solve_tsp()
print("Minimum cost:", cost)
print("Optimal path:", path)
