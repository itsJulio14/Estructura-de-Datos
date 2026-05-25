class LogicaHanoi:
    def __init__(self):
        self.num_discos = 4
        self.torres = {'A': [], 'B': [], 'C': []}
        self.historial_pasos = []
        self.cola_movimientos = []
        self.en_ejecucion = False

    def inicializar_juego(self, num_discos):
        self.num_discos = num_discos
        self.torres['A'] = list(range(num_discos, 0, -1))
        self.torres['B'] = []
        self.torres['C'] = []
        self.historial_pasos = ["Torres inicializadas. Presiona 'Resolver'."]
        self.cola_movimientos = []
        self.en_ejecucion = False

    def generar_plan_resolucion(self):
        """Genera la lista de movimientos usando tu algoritmo recursivo puro"""
        self.cola_movimientos = []
        self._hanoi_recursivo(self.num_discos, 'A', 'B', 'C')
        return self.cola_movimientos

    def _hanoi_recursivo(self, n, origen, auxiliar, destino):
        if n == 1:
            self.cola_movimientos.append((origen, destino))
            return
        self._hanoi_recursivo(n - 1, origen, destino, auxiliar)
        self.cola_movimientos.append((origen, destino))
        self._hanoi_recursivo(n - 1, auxiliar, origen, destino)

    def mover_disco_en_estado(self, origen, destino):
        """Efectúa un único movimiento físico en las pilas internas"""
        if self.torres[origen]:
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.historial_pasos.append(f"Mover disco {disco} de {origen} a {destino}")