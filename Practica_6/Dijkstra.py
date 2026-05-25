import heapq

grafo = {
    0: [(1,9), (4,6)],
    1: [(0,9), (3,8)],
    2: [(5,6), (4,5)],
    3: [(1,8), (5,1), (7,7)],
    4: [(0,6), (2,5), (6,3)],
    5: [(3,1), (2,6)],
    6: [(4,3), (7,2)],
    7: [(6,2), (3,7)]
}

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph} 

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = node 
                heapq.heappush(pq, (distance, neighbor))

    return dist, prev


def reconstruir_camino(prev, start, end):
    camino = []
    actual = end

    while actual is not None:
        camino.append(actual)
        actual = prev[actual]

    camino.reverse()

    if camino[0] == start:
        return camino
    return []


dist, prev = dijkstra(grafo, 0)

for nodo in grafo:
    camino = reconstruir_camino(prev, 0, nodo)
    print(f"0 -> {nodo}: distancia = {dist[nodo]}, camino = {camino}")