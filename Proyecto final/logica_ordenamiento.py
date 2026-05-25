import random

class LogicaOrdenamiento:
    def __init__(self):
        self.lista_base = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]
        # Almacenará tuplas: (lista_en_ese_momento, indice_resaltado_1, indice_resaltado_2)
        self.fotogramas_animacion = []

    def actualizar_lista_desde_texto(self, texto_usuario):
        """Convierte una cadena separada por comas en la lista activa"""
        try:
            valores = [int(x.strip()) for x in texto_usuario.split(",") if x.strip()]
            if not valores:
                return False, "La lista no puede estar vacia"
            self.lista_base = valores
            return True, f"Lista actualizada con {len(valores)} elementos"
        except ValueError:
            return False, "Error: Escribe solo números enteros separados por comas"

    def generar_lista_aleatoria(self, cantidad=10):
        self.lista_base = [random.randint(5, 60) for _ in range(cantidad)]
        return f" Generada lista aleatoria de {cantidad} elementos."

 
    def simular_bubble(self):
        self.fotogramas_animacion = []
        arr = list(self.lista_base)
        n = len(arr)
        
        # Guarda estado inicial
        self.fotogramas_animacion.append((list(arr), -1, -1))
        
        for i in range(n - 1):
            intercambio = False
            for j in range(n - i - 1):
                self.fotogramas_animacion.append((list(arr), j, j + 1))
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    intercambio = True
                    self.fotogramas_animacion.append((list(arr), j, j + 1))
            if not intercambio:
                break
        return self.fotogramas_animacion

    def simular_selection(self):
        self.fotogramas_animacion = []
        arr = list(self.lista_base)
        n = len(arr)
        
        self.fotogramas_animacion.append((list(arr), -1, -1))
        
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                self.fotogramas_animacion.append((list(arr), min_index, j))
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                self.fotogramas_animacion.append((list(arr), i, min_index))
        return self.fotogramas_animacion

    def simular_insertion(self):
        self.fotogramas_animacion = []
        arr = list(self.lista_base)
        
        self.fotogramas_animacion.append((list(arr), -1, -1))
        
        for i in range(1, len(arr)):
            clave = arr[i]
            j = i - 1
            self.fotogramas_animacion.append((list(arr), j, i))
            
            while j >= 0 and arr[j] > clave:
                arr[j + 1] = arr[j]
                self.fotogramas_animacion.append((list(arr), j, j + 1))
                j -= 1
            
            arr[j + 1] = clave
            self.fotogramas_animacion.append((list(arr), j + 1, i))
        return self.fotogramas_animacion

    def simular_merge(self):
        self.fotogramas_animacion = []
        arr = list(self.lista_base)
        self.fotogramas_animacion.append((list(arr), -1, -1))
        
        def _merge_sort_rec(start, end):
            if end - start <= 1:
                return
            medio = (start + end) // 2
            _merge_sort_rec(start, medio)
            _merge_sort_rec(medio, end)
            
            izq = arr[start:medio]
            der = arr[medio:end]
            i = j = 0
            k = start
            
            while i < len(izq) and j < len(der):
                self.fotogramas_animacion.append((list(arr), k, medio + j))
                if izq[i] < der[j]:
                    arr[k] = izq[i]
                    i += 1
                else:
                    arr[k] = der[j]
                    j += 1
                k += 1
                
            while i < len(izq):
                arr[k] = izq[i]
                i += 1
                k += 1
            while j < len(der):
                arr[k] = der[j]
                j += 1
                k += 1
            self.fotogramas_animacion.append((list(arr), start, end - 1))

        _merge_sort_rec(0, len(arr))
        return self.fotogramas_animacion

    def simular_quick(self, usar_aleatorio=False):
        self.fotogramas_animacion = []
        arr = list(self.lista_base)
        self.fotogramas_animacion.append((list(arr), -1, -1))

        def _quick_sort_rec(low, high):
            if low < high:
                if usar_aleatorio:
                    piv_idx = random.randint(low, high)
                    arr[high], arr[piv_idx] = arr[piv_idx], arr[high]
                
                pivote = arr[high]
                i = low - 1
                for j in range(low, high):
                    self.fotogramas_animacion.append((list(arr), j, high))
                    if arr[j] < pivote:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]
                        self.fotogramas_animacion.append((list(arr), i, j))
                        
                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                self.fotogramas_animacion.append((list(arr), i + 1, high))
                
                p_idx = i + 1
                _quick_sort_rec(low, p_idx - 1)
                _quick_sort_rec(p_idx + 1, high)

        _quick_sort_rec(0, len(arr) - 1)
        return self.fotogramas_animacion

    def simular_counting(self):
        self.fotogramas_animacion = []
        arr = list(self.lista_base)
        self.fotogramas_animacion.append((list(arr), -1, -1))
        
        if not arr:
            return self.fotogramas_animacion
            
        max_val = max(arr)
        min_val = min(arr)
        rango = max_val - min_val + 1
        
        conteo = [0] * rango
        salida = [0] * len(arr)
        
        for idx, num in enumerate(arr):
            conteo[num - min_val] += 1
            self.fotogramas_animacion.append((list(arr), idx, -1))
            
        for i in range(1, rango):
            conteo[i] += conteo[i - 1]
            
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            conteo[num - min_val] -= 1
            salida[conteo[num - min_val]] = num
            
            arr[conteo[num - min_val]] = num
            self.fotogramas_animacion.append((list(arr), conteo[num - min_val], i))
            
        self.fotogramas_animacion.append((list(salida), -1, -1))
        return self.fotogramas_animacion