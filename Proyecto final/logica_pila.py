class PilaSimulada:
    def __init__(self):
        self.elementos = []
    
    def push(self, elemento):
        self.elementos.append(elemento)
        
    def pop(self):
        if not self.is_empty():
            return self.elementos.pop()
        return None
        
    def is_empty(self):
        return len(self.elementos) == 0

class LogicaPila:
    def __init__(self):
        self.pila_general = []
        
        self.meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        
        self.datos_productos = {
            "Dulces": [12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75],
            "Conservas": [9800.0, 10150.25, 11200.0, 10950.6, 12010.0, 12500.0, 13120.7, 12890.0, 12330.3, 11990.0, 11500.0, 12750.0],
            "Bebidas": [14320.75, 13990.1, 15005.0, 15540.4, 14890.0, 16010.1, 17005.55, 16800.0, 15990.0, 15450.0, 14900.8, 16500.0]
        }
        
        self.pila_resultado = PilaSimulada()
        self.cola_simulada = []

    def push_general(self, elemento):
        if not elemento.strip():
            return "Error: No puedes agregar un elemento vacío."
        self.pila_general.append(elemento)
        return f"Insertado en la pila (Push): '{elemento}'"

    def pop_general(self):
        if not self.pila_general:
            return "Error: La pila está vacía (Underflow)."
        elemento = self.pila_general.pop()
        return f"Sacado de la pila (Pop): '{elemento}'"

    def ver_pila_general(self):
        if not self.pila_general:
            return "La pila general está vacía."
        pila_visual = "\n".join([f"[ {elem} ]" for elem in reversed(self.pila_general)])
        return f"Estado actual de la Pila:\n{pila_visual}"

    def ordenar_a_pila(self, categoria):
        """Aplica de forma exacta tu algoritmo iterativo de ordenamiento"""
        self.cola_simulada = list(self.datos_productos[categoria])
        self.pila_resultado = PilaSimulada()
        
        historial_pasos = []
        historial_pasos.append(f"--- ORDENANDO CATEGORÍA: {categoria.upper()} ---")
        historial_pasos.append(f"Cola Inicial:\n{self.cola_simulada}\n")

        while self.cola_simulada:
            min_val = self.cola_simulada[0]
            es_menor = True

            for i in range(len(self.cola_simulada)):
                if self.cola_simulada[i] < min_val:
                    es_menor = False
                    break

            if es_menor:
                self.pila_resultado.push(self.cola_simulada.pop(0))
            else:
                self.cola_simulada.append(self.cola_simulada.pop(0))
                
        historial_pasos.append("Ordenamiento Completado de menor a mayor")
        historial_pasos.append(f"Resultado en Pila (.elementos):\n{self.pila_resultado.elementos}")
        return "\n".join(historial_pasos)

    def obtener_reporte_completo(self):
        """Devuelve una cadena tabulada con las listas originales para que el usuario las compare"""
        reporte = "LISTAS DE VENTAS ORIGINALES POR MES:\n\n"
        reporte += f"{'Mes':<12} | {'Dulces':<12} | {'Conservas':<12} | {'Bebidas':<12}\n"
        reporte += "-" * 55 + "\n"
        for i in range(12):
            reporte += f"{self.meses[i]:<12} | ${self.datos_productos['Dulces'][i]:<11} | ${self.datos_productos['Conservas'][i]:<11} | ${self.datos_productos['Bebidas'][i]:<11}\n"
        return reporte