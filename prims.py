import heapq
def prims_algorithm(graph, vertices):
    key = [float('inf')] * vertices
    parent = [-1] * vertices  
    key[0] = 0  
    mst_set = [False] * vertices  
    min_heap = [(0, 0)]  
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if mst_set[u]:
            continue
        mst_set[u] = True
        for v, weight_uv in graph[u]:
            if not mst_set[v] and weight_uv < key[v]:
                key[v] = weight_uv
                parent[v] = u
                heapq.heappush(min_heap, (key[v], v))
    total_weight = sum(key)
    return parent, total_weight
def print_mst(parent, graph):
    print("Edges in the Minimum Spanning Tree:")
    for i in range(1, len(parent)):
        u = parent[i]
        for v, weight in graph[u]:
            if v == i:  
                print(f"{u} -- {v} == {weight}")
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}
vertices = 5
parent, total_weight = prims_algorithm(graph, vertices)
print_mst(parent, graph)
print(f"Total weight of the Minimum Spanning Tree: {total_weight}")
