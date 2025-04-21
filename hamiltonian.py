def is_safe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True
def hamiltonian_cycle_util(graph, path, pos):
    V = len(graph)
    if pos == V:
        return graph[path[pos - 1]][path[0]] == 1
    for v in range(1, V):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1  
    return False
def hamiltonian_cycle(graph):
    V = len(graph)
    path = [-1] * V
    path[0] = 0  
    if not hamiltonian_cycle_util(graph, path, 1):
        print("No Hamiltonian Cycle exists.")
        return False
    path.append(path[0])
    print("Hamiltonian Cycle found:")
    print(" -> ".join(str(v) for v in path))
    return True
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
hamiltonian_cycle(graph)
