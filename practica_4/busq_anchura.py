from collections import deque

def BFS(graph, raiz):
    cola = deque(raiz)
    resultado = []

    print("cola:", list(cola))

    while len(cola)>0:
        nodos_nivel = len(cola)
        siguiente_nivel = []
        
        for i in range(nodos_nivel):
            nodo = cola.popleft()
            resultado.append(nodo)
            
            for hijo in grafo[nodo]:
                siguiente_nivel.append(hijo)
            
        cola.extend(siguiente_nivel)

        if len(cola)>0:
            print("cola:", list(cola))

    return resultado

grafo = {
    'A': ["B", "C"],
    'B': ["D", "E"],
    'C': ["F", "G"],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

arbol = BFS(grafo, "A")
print("\nResultado:", arbol)