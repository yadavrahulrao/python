from collections import defaultdict, deque
def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in range(vertices)}
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(topo_order) != vertices:
        raise ValueError("The graph is not a DAG (contains a cycle)")
    return topo_order
if __name__ == "__main__":
    vertices = 6
    edges = [
        (5, 2), (5, 0),
        (4, 0), (4, 1),
        (2, 3), (3, 1)
    ]
    order = topological_sort(vertices, edges)
    print("Topological Order:", order)
