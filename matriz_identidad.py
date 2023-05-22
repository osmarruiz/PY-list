filas = 4
columnas = 4

matriz_identidad = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad.append(fila)

# Imprimir la matriz
for fila in matriz_identidad:
    print(fila)
