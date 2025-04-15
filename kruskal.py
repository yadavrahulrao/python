class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]
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
def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])  
    disjoint_set = DisjointSet(vertices)
    
    mst = []  
    mst_weight = 0  
  
    for u, v, weight in edges:
      
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight
    
    return mst, mst_weight

vertices = 4 
edges = [
    (0, 1, 10),  
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, total_weight = kruskal(vertices, edges)

print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

print(f"Total weight of the Minimum Spanning Tree: {total_weight}")
