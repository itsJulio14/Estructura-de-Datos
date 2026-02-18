import math
import pandas as pd

# Leer un archivo CSV
df = pd.read_csv('./Housing.csv')
# df = pd.read_csv('Practica_2/Housing.csv')

# Visualizar las primeras filas
# print(df.head())

listaPrecio = list(df['price'])
# print(listaPrecio)


# media = sum(listaPrecio) / len(listaPrecio)
suma=0
for i in listaPrecio:
    suma +=i
media = suma/len(listaPrecio)


frecuencias = {}
for numero in listaPrecio:
    if numero in frecuencias:
        frecuencias[numero] += 1
    else:
        frecuencias[numero] = 1

moda = max(frecuencias, key=frecuencias.get)
# print(set(frecuencias.values()))
# print(max(frecuencias))



sumaDes  = 0
for x in listaPrecio:
    sumaDes +=(x- media) ** 2

varianza = sumaDes / len(listaPrecio)-1
desviacion_Est  = math.sqrt(sumaDes / len(listaPrecio)-1)

print("Media:", media)
print("Moda:", moda,)
print("Varianza", varianza)
print("Desviación media:", desviacion_Est)
