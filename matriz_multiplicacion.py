def multiplicar_matriz(matriz, numero):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            producto = matriz[i][j] * numero
            fila.append(producto)
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


# Obtener las dimensiones de la matriz del usuario
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Ingresar los elementos de la matriz
print("Ingrese los elementos de la matriz:")
matriz = ingresar_matriz(filas, columnas)

# Obtener el número para multiplicar la matriz
numero = int(input("Ingrese el número para multiplicar la matriz: "))

# Multiplicar la matriz por el número
resultado = multiplicar_matriz(matriz, numero)

# Imprimir el resultado
print("La matriz resultante es:")
for fila in resultado:
    print(fila)
