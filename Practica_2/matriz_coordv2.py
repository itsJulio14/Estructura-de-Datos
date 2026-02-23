A = [
    [4, 7, 2, 9, 5, 7],
    [1, 3, 7, 6, 8, 0],
    [9, 2, 5, 7, 4, 6],
    [8, 7, 1, 3, 7, 2],
    [5, 0, 6, 4, 2, 9],
    [7, 8, 9, 2, 1, 7]
]

def buscar_matriz(matriz, x):
    listaCoord=[]


    for fila in range(len(A)):
        for col in range(len(A[fila])):
            if A[fila][col] == x:
                listaCoord.append((fila+1, col+1))

    if listaCoord ==[]:
        print("no encontrado")
    else:
        return listaCoord

x = int(input("Ingrese el numero a buscar: "))

print(buscar_matriz(A,x))