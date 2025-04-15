import heapq
def dijkstra(graph, source, vertices):
    distances = [float('inf')] * vertices
    distances[source] = 0  
    pq = [(0, source)]  
    while pq:
        current_distance, u = heapq.heappop(pq)
        if current_distance > distances[u]:
            continue
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return distances
def print_shortest_paths(distances):
    print("Vertex \tShortest Distance from Source")
    for vertex, distance in enumerate(distances):
        print(f"{vertex} \t\t {distance}")
graph = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 1), (1, 2), (3, 8)],
    3: [(1, 5), (2, 8)]
}
vertices = 4  
source = 0
distances = dijkstra(graph, source, vertices)
print_shortest_paths(distances)
