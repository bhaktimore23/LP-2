from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]
        traversal = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return traversal

    def dfs(self, start):
        visited = set()
        traversal = []

        def dfs_util(vertex):
            visited.add(vertex)
            traversal.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        return traversal


# Example usage:
# Create a graph

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)


# Perform BFS starting from vertex 0
bfs_traversal = g.bfs(0)
print("BFS Traversal:", bfs_traversal)

# Perform DFS starting from vertex 0
dfs_traversal = g.dfs(0)
print("DFS Traversal:", dfs_traversal)