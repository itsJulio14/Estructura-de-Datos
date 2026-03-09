from collections import deque

def vaciar_cola(cola):
    print("Vaciar la cola...")
    while len(cola) > 0:
        print("Cola: ", list(cola))
        cola.popleft()

def reordenar_cola(cola, trans_extra):
    print("Reordenar la cola...")
    while trans_extra > 0:
        x = cola.popleft()
        cola.append(x)
        trans_extra -= 1

lista=[
    (1,0),
    (2,2),
    (3,4),
    (4,6),
    (5,12)

]

cola=deque()
tiempo_max=10
trans_extra=0

for peticion, tiempo in lista:

    if tiempo > tiempo_max:
        #reordenar la cola
        reordenar_cola(cola, trans_extra)
        print(list(cola))
        #vaciar la cola
        vaciar_cola(cola)
        print("cola vacia")
        tiempo_max+=10

    if tiempo <= tiempo_max:
        if len(cola)==3:
            cola.popleft()
            cola.appendleft(peticion)
            trans_extra+=1
        else:
            cola.append(peticion)
        print("Cola:", list(cola))
 

print(list(cola))