import pila;

def enque(lista, elemento):
    lista.append(elemento)

def deque(lista):
    lista.pop(0)

def peek(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False

def size(lista):
    return len(lista)

def ordenarApila(cola, pila):
    while cola:
        min = cola[0]  
        es_menor = True

        for i in range(len(cola)):
            if cola[i] < min:
                es_menor = False
                break

        if es_menor:
            pila.push(cola.pop(0))
        else:
            cola.append(cola.pop(0))

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dulces=[12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75]
Conservas=[9800.0, 10150.25, 11200.0, 10950.6, 12010.0, 12500.0, 13120.7, 12890.0, 12330.3, 11990.0, 11500.0, 12750.0]
Bebidas=[14320.75, 13990.1, 15005.0, 15540.4, 14890.0, 16010.1, 17005.55, 16800.0, 15990.0, 15450.0, 14900.8, 16500.0]

pila_dulce = pila.pila()
cola = []
for i in dulces:
    enque(cola, i)


print(cola)
ordenarApila(cola,pila_dulce)

print(pila_dulce.elementos)

