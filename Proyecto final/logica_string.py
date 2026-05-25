class LogicaString:
    def contar_frecuencia_caracteres(self, cadena):
        if not cadena:
            return "Error: La cadena está vacía."
            
        caracteres_unicos = list(set(cadena))
        caracteres_unicos.sort()
        
        resultado = f"Cadena analizada: '{cadena}'\n\nFrecuencia de caracteres:\n"
        
        total_unicos = len(caracteres_unicos)
        indice = 0
        while indice < total_unicos:
            caracter = caracteres_unicos[indice]
            total_repeticiones = cadena.count(caracter)
            
            vis_caracter = f"'{caracter}'" if caracter == " " else caracter
            resultado += f"{vis_caracter} : {total_repeticiones}\n"
            
            indice += 1
            
        return resultado