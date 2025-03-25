#Dsa Adjancency matrix implementation Of graph
#Assignment 22
#1. Write a class Graph to implement adjacency matrix representation of a simple and
# undirected graph.
#2. In class Graph, define __init__ method to initialise vertex_count and adj_matrix(list of lists)
class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_matrix = [[0]*vno for e in range(vno)]

#3. In class Graph, define add_edge() method add an edge in the graph with given
# weight.
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")

#4. In class Graph, define remove_edge() method to remove an edge from the graph.
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")

#5.In class Graph, define has_edge() method to check whether two given vertices are
#connected by an edge or not.
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] !=0
        else:
            print("Invalid vertex")

#6. In class Graph, define print_adj_matrix() method to print adjacency matrix.
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(' '.join(map(str,row_list)))

g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)

g.print_adj_matrix()