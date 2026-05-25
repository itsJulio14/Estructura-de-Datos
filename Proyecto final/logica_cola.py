class LogicaCola:
    def __init__(self):
        self.cola_general = []
        
        self.saldos = [1000, 1000, 1000, 1000, 1000]
        self.retiros = []
        self.depositos = []

    def enqueue(self, elemento):
        if not elemento.strip():
            return "Error: No puedes agregar un elemento vacio."
        self.cola_general.append(elemento)
        return f"Agregado a la cola: '{elemento}'"

    def dequeue(self):
        if not self.cola_general:
            return "Error: La cola esta vacia"
        elemento = self.cola_general.pop(0)
        return f"Sacado de la cola: '{elemento}'"

    def ver_cola(self):
        if not self.cola_general:
            return "La cola general está vacia"
        return f"Estado actual de la cola:\n{self.cola_general}"

    # --- LÓGICA SIMULACIÓN BANCO ---
    def retiro_w(self, cant_texto):
        if not self.saldos:
            return "Error: No hay cuentas o saldos en la cola del banco"
        try:
            cant = float(cant_texto)
        except ValueError:
            return "Error: Ingresa una cantidad numérica válida"

        dinero = self.saldos.pop(0)
        dinero_restante = dinero - cant
        
        self.retiros.append(cant)
        self.saldos.append(dinero_restante)
        
        return f"Retiro exitoso de ${cant}\nSaldo anterior: ${dinero}\nNuevo saldo enviado al final: ${dinero_restante}"

    def deposito_w(self, cant_texto):
        if not self.saldos:
            return "Error"
        try:
            cant = float(cant_texto)
        except ValueError:
            return "Error"

        dinero = self.saldos.pop(0) 
        dinero_actualizado = dinero + cant
        
        self.depositos.append(cant)
        self.saldos.append(dinero_actualizado)
        
        return f"Deposito Exitoso de ${cant}\nSaldo anterior: ${dinero}\nNuevo saldo enviado al final${dinero_actualizado}"

    def ver_estado_banco(self):
        return (
            f"--- ESTADO DEL BANCO (Vistas en Cola) ---\n\n"
            f"Cola de Saldos (Próximo a atender primero):\n{self.saldos}\n\n"
            f"Historial de Retiros:\n{self.retiros}\n\n"
            f"Historial de Depósitos:\n{self.depositos}"
        )