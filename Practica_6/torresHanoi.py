def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    # Mover n-1 discos de origen a auxiliar
    hanoi(n - 1, origen, destino, auxiliar)
    
    # Mover el disco restante a destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Mover los n-1 discos de auxiliar a destino
    hanoi(n - 1, auxiliar, origen, destino)

# Ejecutar con 5 discos
hanoi(5, 'A', 'B', 'C')