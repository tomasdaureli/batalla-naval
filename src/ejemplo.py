def buscar_embarcacion(tablero, secuencia, fila, columna):
    # Verificar si la secuencia es válida y completa
    if secuencia == "":
        print("¡Embarcación encontrada!")
        return True
    
    # Verificar los límites del tablero y el primer carácter de la secuencia
    if (fila < 0 or fila >= len(tablero)) or (columna < 0 or columna >= len(tablero[0])) or tablero[fila][columna] != secuencia[0]:
        return False

    # Marcar la celda actual como visitada
    temp = tablero[fila][columna]
    tablero[fila][columna] = "#"

    # Buscar en las celdas vecinas
    encontrado = (buscar_embarcacion(tablero, secuencia[1:], fila-1, columna) or  # Arriba
                 buscar_embarcacion(tablero, secuencia[1:], fila+1, columna) or  # Abajo
                 buscar_embarcacion(tablero, secuencia[1:], fila, columna-1) or  # Izquierda
                 buscar_embarcacion(tablero, secuencia[1:], fila, columna+1))    # Derecha
    
    # Desmarcar la celda actual
    tablero[fila][columna] = temp
    
    return encontrado


# Programa principal
tablero = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

secuencia_busqueda = "FGH"

encontrado = False
filas = len(tablero)
columnas = len(tablero[0])

for fila in range(filas):
    for columna in range(columnas):
        if buscar_embarcacion(tablero, secuencia_busqueda, fila, columna):
            encontrado = True
            break

if not encontrado:
    print("Embarcación no encontrada.")
