class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def kruskal(graph):
    minimum_spanning_tree = []
    edges = sorted(graph)

    union_find = UnionFind(len(edges))

    for weight, u, v in edges:
        if union_find.find(u) != union_find.find(v):
            minimum_spanning_tree.append((u, v, weight))
            union_find.union(u, v)

    return minimum_spanning_tree


# Example usage:
graph = [
    (2, 0, 1),  # Edge 0: (weight, u, v)
    (1, 1, 2),  # Edge 1: (weight, u, v)
    (3, 0, 2),  # Edge 2: (weight, u, v)
    (4, 1, 3)   # Edge 3: (weight, u, v)
]

minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    print(edge)
