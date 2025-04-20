def is_safe(node, graph, color, c):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and color[neighbor] == c:
            return False
    return True
def graph_coloring_util(graph, m, color, node):
    if node == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring_util(graph, m, color, node + 1):
                return True
            color[node] = 0  
    return False
def graph_coloring(graph, m):
    color = [0] * len(graph)
    if not graph_coloring_util(graph, m, color, 0):
        print("No solution exists.")
        return False
    print("Color assignment possible:")
    for vertex, c in enumerate(color):
        print(f"Vertex {vertex} --> Color {c}")
    return True
graph = [
    [0, 1, 1, 1],  
    [1, 0, 1, 0],
    [1, 1, 0, 1], 
    [1, 0, 1, 0]   
]
m = 3  
graph_coloring(graph, m)