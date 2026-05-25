class DisjointSet:
    def __init__(self, n):
        # Al principio, cada nodo es su propio padre (raíz)
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        # Encuentra la raíz del conjunto al que pertenece el nodo 'i'
        # Aplica compresión de caminos para futuras búsquedas más rápidas
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Une los conjuntos de 'i' y 'j' según sus rangos
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False  # Ya estaban en el mismo conjunto (formarían un ciclo)


def kruskal(num_vertices, aristas):
    """
    aristas: Lista de tuplas (peso, u, v) donde 'u' y 'v' son los nodos conectados.
    """
    # 1. Ordenar las aristas por su peso de menor a mayor
    aristas_ordenadas = sorted(aristas, key=lambda item: item[0])
    
    ds = DisjointSet(num_vertices)
    mst = []
    costo_total = 0

    # 2. Recorrer las aristas ordenadas
    for peso, u, v in aristas_ordenadas:
        # Si u y v no están en el mismo conjunto, los unimos (no hay ciclo)
        if ds.union(u, v):
            mst.append((u, v, peso))
            costo_total += peso
            
            # Condición de parada: un MST siempre tiene exactamente V - 1 aristas
            if len(mst) == num_vertices - 1:
                break

    return mst, costo_total


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Definimos un grafo con 4 vértices (0, 1, 2, 3)
    # Formato de la arista: (peso, nodo1, nodo2)
    grafo_aristas = [
        (10, 0, 1),
        (6, 0, 2),
        (5, 0, 3),
        (15, 1, 3),
        (4, 2, 3)
    ]
    
    num_vertices = 4
    arbol_minimo, costo = kruskal(num_vertices, grafo_aristas)
    
    print("Aristas en el Árbol de Expansión Mínima (MST):")
    for u, v, peso in arbol_minimo:
        print(f"Nodo {u} -- Nodo {v} con peso: {peso}")
    print(f"\nCosto total del MST: {costo}")
    