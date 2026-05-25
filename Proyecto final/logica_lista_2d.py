class LogicaLista2D:
    @staticmethod
    def parsear_matriz(entrada_texto):
        """Convierte el texto del área de entrada en una matriz de números."""
        try:
            lineas = entrada_texto.strip().split("\n")
            matriz = []
            for linea in lineas:
                if linea.strip():
                    fila = [int(x.strip()) for x in linea.split(",") if x.strip()]
                    matriz.append(fila)
            return matriz
        except ValueError:
            return None

    def multiplicar_matrices(self, texto_x, texto_y):
        x = self.parsear_matriz(texto_x)
        y = self.parsear_matriz(texto_y)

        if not x or not y:
            return "Error: Formato de matriz inválido. Usa números separados por comas"

        if len(x[0]) != len(y):
            return "Error: Las columnas de la Matriz X deben coincidir con las filas de la Matriz Y"

        z = [[0 for _ in range(len(y[0]))] for _ in range(len(x))]
        res = 0

        for fila1 in range(len(x)):
            for col2 in range(len(y[0])):
                for fila2 in range(len(y)):
                    res += (x[fila1][fila2] * y[fila2][col2])
                z[fila1][col2] = res
                res = 0

        resultado_txt = "Resultado de la Multiplicación (Z):\n"
        for fila in z:
            resultado_txt += f"{fila}\n"
        return resultado_txt

    def buscar_numero(self, texto_matriz, numero_buscar):
        matriz = self.parsear_matriz(texto_matriz)
        if not matriz:
            return "Error: Formato de matriz inválido."
        
        try:
            x = int(numero_buscar)
        except ValueError:
            return "Error: Ingresa un número entero válido para buscar."

        lista_coord = []

        for fila in range(len(matriz)):
            for col in range(len(matriz[fila])):
                if matriz[fila][col] == x:
                    lista_coord.append((fila + 1, col + 1))

        if not lista_coord:
            return f"El numero {x} no fue encontrado en la matriz"
        else:
            return f"Numero {x} encontrado en las coordenadas (Fila, Columna):\n{lista_coord}"