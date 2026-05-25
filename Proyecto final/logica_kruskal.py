class LogicaKruskal:
    def __init__(self):
        self.grafo = {
            'Root': [('0', 20), ('3', 20), ('4', 33)],
            '0': [('Root', 20), ('1', 10)],
            '1': [('0', 10), ('3', 50), ('4', 10)],
            '3': [('Root', 20), ('1', 50), ('4', 20), ('5', 2)],
            '4': [('Root', 33), ('1', 10), ('3', 20), ('5', 1)],
            '5': [('4', 1), ('3', 2)]
        }
        self.logs_proceso = []

    def ejecutar_kruskal_completo(self):
        self.logs_proceso = []
        
        self.logs_proceso.append("INICIANDO ALGORITMO DE KRUSKAL (MST)")
        self.logs_proceso.append("Estrategia: Ordenar todas las aristas y aplicar Find-Union.\n")

        aristas = []
        nodos = set()
        for u in self.grafo:
            nodos.add(u)
            for v, peso in self.grafo[u]:
                nodos.add(v)
                if u < v:
                    aristas.append((peso, u, v))
                elif v < u and (peso, v, u) not in aristas:
                    if not any(x[1] == v and x[2] == u for x in aristas):
                        aristas.append((peso, u, v))

        aristas.sort()
        
        self.logs_proceso.append(f"📦 Lista de aristas detectadas y ORDENADAS por peso (Total: {len(aristas)}):")
        for peso, u, v in aristas:
            self.logs_proceso.append(f"   • {u} ─── {v}  (Peso: {peso})")
        self.logs_proceso.append("─" * 60)

        padre = {nodo: nodo for nodo in nodos}

        def find(i):
            if padre[i] == i:
                return i
            padre[i] = find(padre[i])
            return padre[i]

        def union(i, j):
            raiz_i = find(i)
            raiz_j = find(j)
            if raiz_i != raiz_j:
                padre[raiz_i] = raiz_j
                return True
            return False

        mst = []
        for peso, u, v in aristas:
            self.logs_proceso.append(f"Evaluando arista: {u} ─── {v} [Peso: {peso}]")
            
            if union(u, v):
                mst.append((u, v, peso))
                self.logs_proceso.append(f"  Aceptada: Conecta componentes independientes. Añadida al MST.")
            else:
                self.logs_proceso.append(f"  Rechazada: {u} y {v} ya están conectados. ¡Formaría un ciclo!")
            
            self.logs_proceso.append("─" * 60)

        # Resumen de resultados
        total = sum(peso for _, _, peso in mst)
        
        self.logs_proceso.append("\nARISTAS FINALES DEL ÁRBOL DE EXPANSIÓN MÍNIMA (KRUSKAL):")
        self.logs_proceso.append("─" * 60)
        for u, v, w in mst:
            self.logs_proceso.append(f"   🔹 {u} <───> {v}  (Costo: {w})")
            
        self.logs_proceso.append(f"\nCOSTO TOTAL DEL MST GENERADO: {total}")
        return "\n".join(self.logs_proceso)

    def obtener_grafo_texto(self):
        lineas = ["MAPA DE CONEXIONES ORIGINAL DE LA ESTRUCTURA:"]
        for nodo, vecinos in self.grafo.items():
            conexiones = ", ".join([f"({v}, Peso: {p})" for v, p in vecinos])
            lineas.append(f"  Nodo ['{nodo}'] ──> {conexiones}")
        return "\n".join(lineas)