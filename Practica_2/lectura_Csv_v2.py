import pandas as pd
import math

# Leer un archivo CSV
df = pd.read_csv('Practica_2/Housing.csv')

# Seleccionar solo las columnas 
df_numerico = df.select_dtypes(include='number')

def media(lista):
    suma=0
    for i in lista:
        suma +=i
    media = suma/len(lista)
    return media

def moda(lista):
    frecuencias = {}
    for x in lista:
        if x in frecuencias:
            frecuencias[x] += 1
        else:
            frecuencias[x] = 1
    moda = max(frecuencias, key=frecuencias.get)
    return moda

def varianza(lista):
    media2 = media(lista)
    sumaDes = sum((x - media2) ** 2 for x in lista)

    varianza = sumaDes / (len(lista) - 1)  
    return varianza

def desviacionEst(lista):
    var = varianza(lista)
    desviacion_est = math.sqrt(var)
    return desviacion_est



for col in df_numerico.columns[1:]:
    lista = list(df_numerico[col])  # Convertir columna a lista

    print("Columna:",col)
    print("Media:",media(lista))
    print("Moda:",moda(lista))
    print("Varianza",varianza(lista))
    print("Desviacion",desviacionEst(lista))
    print()
