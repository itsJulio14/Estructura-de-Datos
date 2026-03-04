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

def retirosss(lista,lista2):
    r = lista[0]-lista2[0]
    deque(lista)
    deque(lista2)
    enque(lista,r)

def retiro_w(lista,cant):
    dinero = peek(lista)
    deque(lista)
    cant_re = cant
    dinero = dinero-cant_re
    enque(retiro,cant_re)
    enque(saldos,dinero)


def deposito_w(lista,cant):
    dinero = peek(lista)
    deque(lista)
    cant_de = cant
    dinero = dinero+cant_de
    enque(deposito,cant_de)
    enque(saldos,dinero)


saldos = []
retiro = []
deposito = []

enque(saldos,1000)
enque(saldos,1000)
enque(saldos,1000)
enque(saldos,1000)
enque(saldos,1000)

retiro_w(saldos,500)
retiro_w(saldos,500)
retiro_w(saldos,500)
retiro_w(saldos,500)
retiro_w(saldos,500)

deposito_w(saldos,300)
deposito_w(saldos,300)
deposito_w(saldos,300)
deposito_w(saldos,300)
deposito_w(saldos,300)

# enque(retiro,500)
# retirosss(saldos,retiro)

print(saldos)
print(retiro)
print(deposito)
