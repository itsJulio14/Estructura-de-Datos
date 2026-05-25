class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class LogicaNodo:
    def __init__(self):
        self.raiz = None

    def establecer_raiz(self, valor):
        if not valor.strip():
            return "Error: El valor no puede estar vacío."
        if self.raiz is not None:
            return f"La raíz ya existe y es '{self.raiz.valor}'. Borra el árbol para cambiarla."
        self.raiz = Nodo(valor)
        return f"Raíz establecida con éxito: '{valor}'"

    def buscar_nodo(self, actual, valor_buscar):
        """Busca un nodo por su valor usando recursividad"""
        if actual is None:
            return None
        if str(actual.valor) == str(valor_buscar):
            return actual
        
        nodo_izq = self.buscar_nodo(actual.izq, valor_buscar)
        if nodo_izq:
            return nodo_izq
            
        return self.buscar_nodo(actual.der, valor_buscar)

    def agregar_hijo(self, valor_padre, valor_hijo, lado):
        if self.raiz is None:
            return "Error: Primero debes establecer una Raíz para el árbol."
        if not valor_hijo.strip():
            return "Error: El valor del nuevo nodo no puede estar vacío."

        padre = self.buscar_nodo(self.raiz, valor_padre)
        if not padre:
            return f"Error: No se encontró el nodo padre '{valor_padre}'."

        if lado == "izq":
            if padre.izq is not None:
                return f"Error: El nodo '{valor_padre}' ya tiene un hijo izquierdo ('{padre.izq.valor}')."
            padre.izq = Nodo(valor_hijo)
            return f"Nodo '{valor_hijo}' agregado a la IZQUIERDA de '{valor_padre}'."
        else:
            if padre.der is not None:
                return f"Error: El nodo '{valor_padre}' ya tiene un hijo derecho ('{padre.der.valor}')."
            padre.der = Nodo(valor_hijo)
            return f"Nodo '{valor_hijo}' agregado a la DERECHA de '{valor_padre}'."

    def limpiar_arbol(self):
        self.raiz = None
        return "Árbol vaciado por completo."

    def preorden(self, nodo, resultado):
        if nodo:
            resultado.append(str(nodo.valor))
            self.preorden(nodo.izq, resultado)
            self.preorden(nodo.der, resultado)

    def inorden(self, nodo, resultado):
        if nodo:
            self.inorden(nodo.izq, resultado)
            resultado.append(str(nodo.valor))
            self.inorden(nodo.der, resultado)

    def postorden(self, nodo, resultado):
        if nodo:
            self.postorden(nodo.izq, resultado)
            self.postorden(nodo.der, resultado)
            resultado.append(str(nodo.valor))

    def obtener_recorrido(self, tipo):
        if self.raiz is None:
            return "El arbol está vacio."
        resultado = []
        if tipo == "Preorden":
            self.preorden(self.raiz, resultado)
        elif tipo == "Inorden":
            self.inorden(self.raiz, resultado)
        elif tipo == "Postorden":
            self.postorden(self.raiz, resultado)
        return " -> ".join(resultado)

    def obtener_grafico_texto(self):
        if self.raiz is None:
            return "El árbol está vacío."
        lineas, _, _, _ = self._construir_arbol_vistas(self.raiz)
        return "\n".join(lineas)

    def _construir_arbol_vistas(self, nodo):
        """Método helper recursivo para estructurar espacios y ramas visuales"""
        if nodo.der is None and nodo.izq is None:
            linea = f"{nodo.valor}"
            ancho = len(linea)
            alto = 1
            medio = ancho // 2
            return [linea], ancho, alto, medio

        if nodo.der is None:
            lineas, ancho, alto, medio = self._construir_arbol_vistas(nodo.izq)
            s = f"{nodo.valor}"
            long_s = len(s)
            primer_linea = (medio + 1) * " " + (ancho - medio - 1) * "_" + s
            segunda_linea = medio * " " + "/" + (ancho - medio - 1 + long_s) * " "
            lineas_reordenadas = [primer_linea, segunda_linea] + [l + long_s * " " for l in lineas]
            return lineas_reordenadas, ancho + long_s, alto + 2, ancho + long_s // 2

        if nodo.izq is None:
            lineas, ancho, alto, medio = self._construir_arbol_vistas(nodo.der)
            s = f"{nodo.valor}"
            long_s = len(s)
            primer_linea = s + medio * "_" + (ancho - medio) * " "
            segunda_linea = (long_s + medio) * " " + "\\" + (ancho - medio - 1) * " "
            lineas_reordenadas = [primer_linea, segunda_linea] + [long_s * " " + l for l in lineas]
            return lineas_reordenadas, ancho + long_s, alto + 2, long_s // 2

        # Si tiene ambos hijos
        lineas_izq, ancho_izq, alto_izq, medio_izq = self._construir_arbol_vistas(nodo.izq)
        lineas_der, ancho_der, alto_der, medio_der = self._construir_arbol_vistas(nodo.der)
        s = f"{nodo.valor}"
        long_s = len(s)
        primer_linea = (medio_izq + 1) * " " + (ancho_izq - medio_izq - 1) * "_" + s + medio_der * "_" + (ancho_der - medio_der) * " "
        segunda_linea = medio_izq * " " + "/" + (ancho_izq - medio_izq - 1 + long_s + medio_der) * " " + "\\" + (ancho_der - medio_der - 1) * " "
        
        if alto_izq < alto_der:
            lineas_izq += [ancho_izq * " "] * (alto_der - alto_izq)
        elif alto_der < alto_izq:
            lineas_der += [ancho_der * " "] * (alto_izq - alto_der)
            
        lineas_mezcladas = [l_izq + long_s * " " + l_der for l_izq, l_der in zip(lineas_izq, lineas_der)]
        return [primer_linea, segunda_linea] + lineas_mezcladas, ancho_izq + ancho_der + long_s, max(alto_izq, alto_der) + 2, ancho_izq + long_s // 2