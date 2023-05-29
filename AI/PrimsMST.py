import heapq

def prim(graph):
    start_node=next(iter(graph))
    visited=set([start_node])
    
    minimum_spanning_tree=[]
    
    heap=[(weight,start_node, next_node) for next_node, weight in graph[start_node]]
    
    heapq.heapify(heap)
    
    while heap:
        weight,u,v=heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            
            minimum_spanning_tree.append((u,v,weight))
            
            for next_node, next_weight in graph[v]:
                if next_node not in visited:
                    heapq.heappush(heap,(next_weight, v,next_node))
                    
    return minimum_spanning_tree

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 4), ('C', 2)]
}

minimum_spanning_tree=prim(graph)
for edge in minimum_spanning_tree:
    print(edge)
        