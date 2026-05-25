import random
def bubblesort(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if intercambio == False:
            break
    return lista
#-----------------------------------------------------------------------
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
#-----------------------------------------------------------------------
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave
    return lista
#-----------------------------------------------------------------------
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)

def  merge(izq, der):
    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
#-----------------------------------------------------------------------
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
#-----------------------------------------------------------------------
def quick_sort_random(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = random.choice(lista)

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
#-----------------------------------------------------------------------
def counting_sort(lista):
    if not lista:
        return lista
    
    max_val = max(lista)
    min_val = min(lista)
    
    rango = max_val - min_val + 1
    
    conteo = [0] * rango
    salida = [0] * len(lista)
    
    for num in lista:
        conteo[num - min_val] += 1
    
    for i in range(1, rango):
        conteo[i] += conteo[i - 1]
    
    for i in range(len(lista) - 1, -1, -1):
        num = lista[i]
        conteo[num - min_val] -= 1
        salida[conteo[num - min_val]] = num
    return salida
#-----------------------------------------------------------------------


lista = [10,50,23,3,43,23,29,49,12,40]

# print(bubblesort(lista))

# print(selection_sort(lista))

# print(insertion_sort(lista))

# print(merge_sort(lista))

# print(quick_sort(lista))

# print(quick_sort_random(lista))

print(counting_sort(lista))
