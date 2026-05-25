from collections import deque
class LogicaBicola:
    def __init__(self):
        self.bicola_general = []
        
        self.saldos = []
        self.retiros = []
        self.depositos = []
        self.head_index = 0
        self.tail_index = 0
        self.inicializar_banco()

        self.lista_peticiones_iniciales = [(1, 0), (2, 2), (3, 4), (4, 6), (5, 12)]
        self.cola_tiempo = deque()
        self.tiempo_max = 10
        self.trans_extra = 0
        self.historial_pasos = []

    def inicializar_banco(self):
        """Reinicia el banco al estado original del ejemplo"""
        self.saldos = []
        self.retiros = []
        self.depositos = []
        self.head_index = 0
        self.tail_index = 0
        
        self.enque_der(self.saldos, 1000)
        self.enque_der(self.saldos, 1000)
        self.enque_der(self.saldos, 1000)
        self.enque_der(self.saldos, 1000)
        self.enque_izq(self.saldos, 1000)

    def enque_der(self, lista, elemento):
        lista.append(elemento)

    def enque_izq(self, lista, elemento):
        lista.insert(0, elemento)

    def deque_der(self, lista):
        if self.is_empty(lista): return None
        return lista.pop()

    def deque_izq(self, lista):
        if self.is_empty(lista): return None
        return lista.pop(0)

    def peek_der(self, lista):
        return None if self.is_empty(lista) else lista[-1]

    def peek_izq(self, lista):
        return None if self.is_empty(lista) else lista[0]

    def is_empty(self, lista):
        return len(lista) == 0

    def size(self, lista):
        return len(lista)

    def UI_enque_der(self, elemento):
        if not elemento.strip(): return "Error: Elemento vacío."
        self.enque_der(self.bicola_general, elemento)
        return f"Agregado a la Derecha: '{elemento}'"

    def UI_enque_izq(self, elemento):
        if not elemento.strip(): return "Error: Elemento vacío."
        self.enque_izq(self.bicola_general, elemento)
        return f"Agregado a la Izquierda: '{elemento}'"

    def UI_deque_der(self):
        if self.is_empty(self.bicola_general): return "Error: La bicola está vacía."
        val = self.deque_der(self.bicola_general)
        return f"Sacado de la Derecha: '{val}'"

    def UI_deque_izq(self):
        if self.is_empty(self.bicola_general): return "Error: La bicola está vacía."
        val = self.deque_izq(self.bicola_general)
        return f"Sacado de la Izquierda: '{val}'"

    def ver_bicola(self):
        if self.is_empty(self.bicola_general): return "La bicola está vacía."
        return f"Estado de la Bicola:\nFrente [ {', '.join(map(str, self.bicola_general))} ] Final"

    # --- LÓGICA DEL BANCO (HEAD/TAIL) ---
    def head_retiro(self, cant_texto):
        try:
            cant = float(cant_texto)
        except ValueError:
            return "Error: Ingresa una cantidad numérica válida."

        if self.head_index < self.size(self.saldos):
            saldo_anterior = self.saldos[self.head_index]
            self.saldos[self.head_index] -= cant
            self.retiros.append(cant)
            res = f"Retiro de ${cant} en Cuenta Index [{self.head_index}]\nSaldo Anterior: ${saldo_anterior}\nNuevo Saldo: ${self.saldos[self.head_index]}"
            self.head_index += 1
            return res
            
        return "Todos los turnos de Retiro (Head) ya fueron procesados."

    def tail_deposito(self, cant_texto):
        try:
            cant = float(cant_texto)
        except ValueError:
            return "Error: Ingresa una cantidad numérica válida."

        if self.tail_index < self.size(self.saldos):
            index = -(self.tail_index + 1)
            saldo_anterior = self.saldos[index]
            self.saldos[index] += cant
            self.depositos.append(cant)
            idx_positivo = self.size(self.saldos) + index 
            res = f"Depósito de ${cant} en Cuenta Index [{idx_positivo}] (Posición Final {index})\nSaldo Anterior: ${saldo_anterior}\nNuevo Saldo: ${self.saldos[index]}"
            self.tail_index += 1
            return res
            
        return "Todos los turnos de Depósito (Tail) ya fueron procesados."

    def ver_estado_banco(self):
        return (
            f"--- ESTADO DEL BANCO (Bicola de Saldos) ---\n\n"
            f"Cuentas/Saldos Actuales:\n{self.saldos}\n"
            f"Próximo Índice a Retirar (Head): {self.head_index}\n"
            f"Próximo Índice a Depositar (Tail): {self.tail_index} (Inverso)\n\n"
            f"Historial de Retiros: {self.retiros}\n"
            f"Historial de Depósitos: {self.depositos}"
        )
    
    def reiniciar_simulacion_tiempo(self):
        self.cola_tiempo = deque()
        self.tiempo_max = 10
        self.trans_extra = 0
        self.historial_pasos = []

    def _vaciar_cola_tiempo(self):
        self.historial_pasos.append("Vaciar la cola...")
        while len(self.cola_tiempo) > 0:
            self.historial_pasos.append(f"Estado en vaciado: {list(self.cola_tiempo)}")
            self.cola_tiempo.popleft()

    def _reordenar_cola_tiempo(self, trans_extra_actual):
        self.historial_pasos.append("Reordenar la cola...")
        while trans_extra_actual > 0:
            x = self.cola_tiempo.popleft()
            self.cola_append_tiempo(x)
            trans_extra_actual -= 1

    def cola_append_tiempo(self, elemento):
        self.cola_tiempo.append(elemento)

    def ejecutar_simulacion_tiempo(self):
        self.reiniciar_simulacion_tiempo()
        
        for peticion, tiempo in self.lista_peticiones_iniciales:
            self.historial_pasos.append(f"\nEvaluando Petición {peticion} (Tiempo: {tiempo})")
            
            if tiempo > self.tiempo_max:
                self._reordenar_cola_tiempo(self.trans_extra)
                self.historial_pasos.append(f"Cola tras reordenar: {list(self.cola_tiempo)}")
                self._vaciar_cola_tiempo()
                self.historial_pasos.append(f" Cola vacia")
                self.tiempo_max += 10
                self.historial_pasos.append(f"Nuevo tiempo máximo: {self.tiempo_max}")

            if tiempo <= self.tiempo_max:
                if len(self.cola_tiempo) == 3:
                    self.cola_tiempo.popleft()
                    self.cola_tiempo.appendleft(peticion)
                    self.trans_extra += 1
                    self.historial_pasos.append(f"Cola llena. Intercambio realizado. trans_extra: {self.trans_extra}")
                else:
                    self.cola_tiempo.append(peticion)
                
                self.historial_pasos.append(f"Estado de la cola: {list(self.cola_tiempo)}")

        self.historial_pasos.append(f"\nSimulación finalizada. Estado final: {list(self.cola_tiempo)}")
        return "\n".join(self.historial_pasos)