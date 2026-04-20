class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class Arbol:
    def __init__(self, dato_inicial):
        self.raiz: Nodo = Nodo(dato_inicial)

    def agregar(self, dato):
        self._agregar_recursivo(self.raiz, dato)

    def agregar_lista(self, lista):
        for dato in lista:
            self.agregar(dato)

    def _agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.derecho, dato)


def inorden(nodo: Nodo | None):
    if nodo is None:
        return
    # izquierda
    if nodo.izquierdo:
        inorden(nodo.izquierdo)
    else:
        if nodo.derecho:
            print("none", end=",")
    # nodo
    print(nodo.dato, end=",")
    # derecha
    if nodo.derecho:
        inorden(nodo.derecho)

def preorden(nodo: Nodo | None):
    if nodo is None:
        return
    print(nodo.dato, end=",")
    # izquierda
    if nodo.izquierdo:
        preorden(nodo.izquierdo)
    else:
        if nodo.derecho:
            print("none", end=",")
    # derecha
    if nodo.derecho:
        preorden(nodo.derecho)


def postorden(nodo: Nodo | None):
    if nodo is None:
        return
    # izquierda
    if nodo.izquierdo:
        postorden(nodo.izquierdo)
    else:
        if nodo.derecho:
            print("none", end=",")
    # derecha
    if nodo.derecho:
        postorden(nodo.derecho)
    else:
        if nodo.izquierdo:
            print("none", end=",")
    # nodo
    print(nodo.dato, end=",")



arbol = Arbol(3)   # raiz(3)

arbol.agregar_lista([1,4,2,5])


print("\nInorden:")
inorden(arbol.raiz)
print("\nPreorden:")
preorden(arbol.raiz)
print("\nPostorden:")
postorden(arbol.raiz)
