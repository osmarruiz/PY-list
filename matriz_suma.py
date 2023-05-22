def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    
    return resultado


def ingresar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    return matriz


# Obtener las dimensiones de las matrices del usuario
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Ingresar los elementos de la primera matriz
print("Ingrese los elementos de la primera matriz:")
matriz1 = ingresar_matriz(filas, columnas)

# Ingresar los elementos de la segunda matriz
print("Ingrese los elementos de la segunda matriz:")
matriz2 = ingresar_matriz(filas, columnas)

# Sumar las matrices
resultado = sumar_matrices(matriz1, matriz2)


print("La suma de las matrices es:")
for fila in resultado:
    print(fila)
