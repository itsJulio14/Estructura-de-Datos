def enque_der(lista, elemento):
    lista.append(elemento)

def enque_izq(lista, elemento):
    lista.insert(0, elemento)

def deque_der(lista):
    lista.pop()

def deque_izq(lista):
    lista.pop(0)

def peek_der(lista):
    return lista[-1]

def peek_izq(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False

def size(lista):
    return len(lista)


head_index = 0  
tail_index = 0  
def head_retiro(lista, cant):
    global head_index
    if head_index < size(lista):
        lista[head_index] -= cant
        retiro.append(cant)
        head_index += 1 

def tail_deposito(lista, cant):
    global tail_index
    if tail_index < size(lista):
        index = -(tail_index + 1)
        lista[index] += cant
        deposito.append(cant)
        tail_index += 1

saldos = []
retiro = []
deposito = []

enque_der(saldos,1000)
enque_der(saldos,1000)
enque_der(saldos,1000)
enque_der(saldos,1000)
enque_izq(saldos,1000)

head_retiro(saldos,500)
head_retiro(saldos,400)
head_retiro(saldos,300)
head_retiro(saldos,200)
head_retiro(saldos,100)

print(saldos)
print("\n")

tail_deposito(saldos,500)
tail_deposito(saldos,400)
tail_deposito(saldos,300)   
tail_deposito(saldos,200)
tail_deposito(saldos,100)





print(saldos)

