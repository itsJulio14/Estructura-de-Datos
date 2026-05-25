class LogicaLista:
    @staticmethod
    def limpiar_datos(entrada):
        items = [i.strip() for i in entrada.split(",") if i.strip()]
        procesados = []
        for x in items:
            try:
                procesados.append(float(x) if "." in x else int(x))
            except ValueError:
                procesados.append(x)
        return procesados

    def sacar_promedio(self, entrada):
        lista = [x for x in self.limpiar_datos(entrada) if isinstance(x, (int, float))]
        if not lista: return "Error: No hay numeros"
        return sum(lista) / len(lista)

    def eliminar_repetidos(self, entrada):
        lista = self.limpiar_datos(entrada)
        return list(dict.fromkeys(lista))

    def contar_elementos(self, entrada):
        lista = self.limpiar_datos(entrada)
        return f"Total: {len(lista)} elementos"

    def clasificar_por_promedio(self, entrada):
        lista = [x for x in self.limpiar_datos(entrada) if isinstance(x, (int, float))]
        
        if not lista: 
            return "Error: No hay números válidos"
            
        promedio = sum(lista) / len(lista)
        lista_mayor = []
        lista_menor = []
        
        for i in lista:
            if i > promedio:
                lista_mayor.append(i)
            else:
                lista_menor.append(i)
                
        return f"Promedio: {promedio:.2f}\n\nMayores al promedio:\n{lista_mayor}\n\nMenores/Iguales al promedio:\n{lista_menor}"