import heapq

class LogicaPrim:
    def __init__(self):
        # Tu grafo original para Prim
        self.grafo = {
            'Root': [('0', 20), ('3', 20), ('4', 33)],
            '0': [('Root', 20), ('1', 10)],
            '1': [('0', 10), ('3', 50), ('4', 10)],
            '3': [('Root', 20), ('1', 50), ('4', 20), ('5', 2)],
            '4': [('Root', 33), ('1', 10), ('3', 20), ('5', 1)],
            '5': [('4', 1), ('3', 2)]
        }
        self.logs_proceso = []

    def ejecutar_prim_completo(self, inicio='Root'):
        self.logs_proceso = []
        
        # Validación de formateo rápido por si el usuario escribe en minúsculas
        if inicio.lower() == 'root':
            inicio = 'Root'
            
        if inicio not in self.grafo:
            return f"❌ Error: El nodo '{inicio}' no existe en el grafo."

        self.logs_proceso.append("🎬 INICIANDO ALGORITMO DE PRIM (MST)")
        self.logs_proceso.append(f"Nodo de inicio seleccionado: '{inicio}'\n")
        self.logs_proceso.append("─" * 55)

        # Tu algoritmo base con inyección de logs
        visitados = set()
        mst = []
        heap = [(0, inicio, None)]

        while heap:
            peso, nodo, padre = heapq.heappop(heap)
            
            if nodo in visitados:
                self.logs_proceso.append(f" ⏭️ Saltado '{nodo}': Ya se encuentra en el conjunto visitado.")
                continue

            visitados.add(nodo)
            self.logs_proceso.append(f" 📥 Expandiendo Nodo '{nodo}' (Peso acumulado arista: {peso})")

            if padre is not None:
                mst.append((padre, nodo, peso))
                self.logs_proceso.append(f"    ✅ Arista aceptada en MST: {padre} ──({peso})──> {nodo}")

            for vecino, costo in self.grafo[nodo]:
                if vecino not in visitados:
                    heapq.heappush(heap, (costo, vecino, nodo))
                    self.logs_proceso.append(f"       🔍 Descubierta opción: Hacia '{vecino}' con peso {costo}")
            
            self.logs_proceso.append("─" * 55)

        # Calcular costo total e imprimir resumen
        total = sum(peso for _, _, peso in mst)
        
        self.logs_proceso.append("\n🌲 ARISTAS FINALES DEL ÁRBOL DE EXPANSIÓN MÍNIMA (MST):")
        self.logs_proceso.append("─" * 55)
        for u, v, w in mst:
            self.logs_proceso.append(f"   🔹 {u} <───> {v}  (Costo: {w})")
            
        self.logs_proceso.append(f"\n💰 PESO TOTAL DEL MST: {total}")
        return "\n".join(self.logs_proceso)

    def obtener_grafo_texto(self):
        lineas = ["🗺️ MAPA DE CONEXIONES Y PESOS DEL GRAFO (PRIM):"]
        for nodo, vecinos in self.grafo.items():
            conexiones = ", ".join([f"({v}, Peso: {p})" for v, p in vecinos])
            lineas.append(f"  Nodo ['{nodo}'] ──> {conexiones}")
        return "\n".join(lineas)