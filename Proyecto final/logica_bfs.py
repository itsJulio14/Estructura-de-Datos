from collections import deque

class LogicaBFS:
    def __init__(self):
        self.grafo = {
            'A': ["B", "C"],
            'B': ["D", "E"],
            'C': ["F", "G"],
            'D': [],
            'E': [],
            'F': [],
            'G': []
        }
        self.logs_proceso = []

    def ejecutar_bfs(self, nodo_raiz):
        self.logs_proceso = []
        nodo_raiz = nodo_raiz.upper().strip()

        if nodo_raiz not in self.grafo:
            return f"Error: El nodo '{nodo_raiz}' no existe en el grafo actual."

        cola = deque([nodo_raiz])
        resultado = []

        self.logs_proceso.append("INICIANDO RECORRIDO EN ANCHURA (BFS)")
        self.logs_proceso.append(f"Cola inicial: {list(cola)}\n")
        self.logs_proceso.append("─" * 45)

        paso = 1
        while len(cola) > 0:
            nodos_nivel = len(cola)
            siguiente_nivel = []
            
            self.logs_proceso.append(f"Paso {paso}: Procesando nivel actual con {nodos_nivel} nodo(s).")
            
            for i in range(nodos_nivel):
                nodo = cola.popleft()
                resultado.append(nodo)
                self.logs_proceso.append(f" Extrayendo '{nodo}' de la cola. Agregado al resultado.")
                
                for hijo in self.grafo[nodo]:
                    siguiente_nivel.append(hijo)
                    self.logs_proceso.append(f" Descubierto hijo: '{hijo}' (se encola para el sig. nivel)")
            
            cola.extend(siguiente_nivel)
            
            self.logs_proceso.append(f"Estado de la cola al terminar el nivel: {list(cola)}")
            self.logs_proceso.append("─" * 45)
            paso += 1

        self.logs_proceso.append(f"\n ¡Simulación Terminada!")
        self.logs_proceso.append(f" Resultado Final (Orden de Visita): {resultado}")
        
        return "\n".join(self.logs_proceso)

    def obtener_conexiones_texto(self):
        """Muestra el mapeo de adyacencia actual"""
        lineas = ["MAPA DE CONEXIONES DEL GRAFO (Diccionario):"]
        for nodo, hijos in self.grafo.items():
            conexiones = ", ".join(hijos) if hijos else "Ninguno (Nodo Hoja)"
            lineas.append(f"  Node [{nodo}] conectado hacia ──> [{conexiones}]")
        return "\n".join(lineas)