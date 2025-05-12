from collections import deque, defaultdict

def bfs(capacity, graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and capacity[u][v] > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    return False

def edmonds_karp(graph, source, sink):
    # Initialize capacities
    capacity = defaultdict(lambda: defaultdict(int))
    for u in graph:
        for v in graph[u]:
            capacity[u][v] = graph[u][v]

    parent = {}
    max_flow = 0

    while bfs(capacity, graph, source, sink, parent):
        # Find bottleneck capacity
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

# Example usage
if __name__ == "__main__":
    graph = {
        'S': {'A': 10, 'C': 10},
        'A': {'B': 4, 'C': 2},
        'B': {'D': 10},
        'C': {'D': 8},
        'D': {}
    }

    source = 'S'
    sink = 'D'
    max_flow = edmonds_karp(graph, source, sink)
    print(f"Maximum flow: {max_flow}")

