class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Recorrido en Preorden: Raíz -> Izquierda -> Derecha
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

# Recorrido en Inorden: Izquierda -> Raíz -> Derecha
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        inorden(nodo.derecho)

# Recorrido en Postorden: Izquierda -> Derecha -> Raíz
def postorden(nodo):
    if nodo:
        postorden(nodo.izquierdo)
        postorden(nodo.derecho)
        print(nodo.valor, end=" ")

# --- Ejemplo de uso ---
#      1
#     / \
#    2   3
#   / \
#  4   5
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("Preorden: "); preorden(raiz)    # 1 2 4 5 3
print("\nInorden: "); inorden(raiz)     # 4 2 5 1 3
print("\nPostorden: "); postorden(raiz) # 4 5 2 3 1