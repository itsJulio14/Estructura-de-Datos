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


lista =[]
# print(is_empty(lista))
enque(lista,1)
print(lista)
print(is_empty(lista))
deque(lista)
print(is_empty(lista))
enque(lista,8)
enque(lista,131)
deque(lista)
enque(lista,0)

print(lista)
