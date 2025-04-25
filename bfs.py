from collections import deque, defaultdict
def bfs_shortest_paths(graph, source):
    visited = set()
    distance = {}
    parent = {}
    queue = deque()
    queue.append(source)
    visited.add(source)
    distance[source] = 0
    parent[source] = None
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
    return distance, parent
def reconstruct_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    source = 'A'
    distance, parent = bfs_shortest_paths(graph, source)
    print("Shortest distances from source:", source)
    for node in graph:
        print(f"  {node}: {distance.get(node, 'Unreachable')}")
    print("\nPaths from source:")
    for node in graph:
        path = reconstruct_path(parent, node)
        print(f"  Path to {node}: {' -> '.join(path)}")
