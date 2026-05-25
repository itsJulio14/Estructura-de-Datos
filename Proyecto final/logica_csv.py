import pandas as pd
import math
import os

class LogicaCSV:
    def media(self, lista):
        suma = 0
        for i in lista:
            suma += i
        return suma / len(lista)

    def moda(self, lista):
        frecuencias = {}
        for x in lista:
            if x in frecuencias:
                frecuencias[x] += 1
            else:
                frecuencias[x] = 1
        return max(frecuencias, key=frecuencias.get)

    def varianza(self, lista):
        media2 = self.media(lista)
        sumaDes = sum((x - media2) ** 2 for x in lista)
        return sumaDes / (len(lista) - 1)  

    def desviacion_est(self, lista):
        var = self.varianza(lista)
        return math.sqrt(var)

    def analizar_csv(self, ruta_archivo):
        if not os.path.exists(ruta_archivo):
            return f"Error: No se encontró el archivo en la ruta:\n{ruta_archivo}"
        
        try:
            # Leer archivo CSV
            df = pd.read_csv(ruta_archivo)
            
            # Seleccionar solo las columnas numéricas
            df_numerico = df.select_dtypes(include='number')
            
            if df_numerico.empty:
                return "Error: El archivo CSV no contiene columnas numéricas."
                
            resultado_txt = f"Análisis del archivo: {os.path.basename(ruta_archivo)}\n"
            resultado_txt += "="*40 + "\n\n"
            
            # Tu bucle original (analizando desde la segunda columna numérica en adelante)
            columnas_a_procesar = df_numerico.columns[1:]
            
            if len(columnas_a_procesar) == 0:
                # Si solo hay una columna numérica, procesamos esa en su lugar
                columnas_a_procesar = df_numerico.columns

            for col in columnas_a_procesar:
                lista = list(df_numerico[col].dropna())  # Convertir a lista eliminando nulos
                
                if not lista:
                    continue
                    
                resultado_txt += f"Columna: {col}\n"
                resultado_txt += f"  > Media: {self.media(lista):.4f}\n"
                resultado_txt += f"  > Moda: {self.moda(lista)}\n"
                resultado_txt += f"  > Varianza: {self.varianza(lista):.4f}\n"
                resultado_txt += f"  > Desviación Est.: {self.desviacion_est(lista):.4f}\n"
                resultado_txt += "-"*30 + "\n"
                
            return resultado_txt

        except Exception as e:
            return f"Error al procesar el archivo CSV:\n{str(e)}"