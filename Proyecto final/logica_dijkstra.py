import heapq

class LogicaDijkstra:
    def __init__(self):
        self.grafo = {
            0: [(1, 9), (4, 6)],
            1: [(0, 9), (3, 8)],
            2: [(5, 6), (4, 5)],
            3: [(1, 8), (5, 1), (7, 7)],
            4: [(0, 6), (2, 5), (6, 3)],
            5: [(3, 1), (2, 6)],
            6: [(4, 3), (7, 2)],
            7: [(6, 2), (3, 7)]
        }
        self.logs_proceso = []

    def ejecutar_y_reconstruir(self, start):
        self.logs_proceso = []
        
        if start not in self.grafo:
            return f"Error: El nodo {start} no existe en el grafo."

        dist, prev = self._dijkstra(start)

        self.logs_proceso.append("\nRESULTADOS FINALES DE RUTAS ÓPTIMAS:")
        self.logs_proceso.append("─" * 50)
        
        for nodo in self.grafo:
            camino = self._reconstruir_camino(prev, start, nodo)
            camino_str = " -> ".join(map(str, camino)) if camino else "No alcanzable"
            self.logs_proceso.append(
                f" {start} ──> {nodo} | Distancia minima = {dist[nodo]} | Camino = [{camino_str}]"
            )
            
        return "\n".join(self.logs_proceso)

    def _dijkstra(self, start):
        dist = {node: float('inf') for node in self.grafo}
        prev = {node: None for node in self.grafo} 

        dist[start] = 0
        pq = [(0, start)]

        self.logs_proceso.append("INICIANDO ALGORITMO DE DIJKSTRA")
        self.logs_proceso.append(f"Punto de partida establecido en el Nodo: {start}\n")
        self.logs_proceso.append("─" * 50)

        while pq:
            current_dist, node = heapq.heappop(pq)
            self.logs_proceso.append(f"Extrado de la Cola de Prioridad: Nodo {node} (Distancia acumulada: {current_dist})")

            if current_dist > dist[node]:
                self.logs_proceso.append(f" Saltado: Ya se encontro un camino más corto hacia {node}")
                continue

            for neighbor, weight in self.grafo[node]:
                distance = current_dist + weight
                self.logs_proceso.append(f" Evaluando vecino {neighbor}: {current_dist} + peso {weight} = {distance}")

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = node 
                    heapq.heappush(pq, (distance, neighbor))
                    self.logs_proceso.append(f" Camino mejorado, Nueva distancia a {neighbor} es {distance}. Encolado.")

            self.logs_proceso.append("─" * 50)

        return dist, prev

    def _reconstruir_camino(self, prev, start, end):
        camino = []
        actual = end

        while actual is not None:
            camino.append(actual)
            actual = prev[actual]

        camino.reverse()

        if camino and camino[0] == start:
            return camino
        return []

    def obtener_grafo_texto(self):
        """Muestra las conexiones y pesos actuales del diccionario"""
        lineas = ["MATRIZ/DICCIONARIO DE ADYACENCIA CON PESOS:"]
        for nodo, vecinos in self.grafo.items():
            conexiones = ", ".join([f"(Destino: {v}, Peso: {p})" for v, p in vecinos])
            lineas.append(f"  Nodo [{nodo}] conectado a ──> {conexiones if conexiones else 'Ninguno'}")
        return "\n".join(lineas)