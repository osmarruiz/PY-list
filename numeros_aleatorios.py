import random
def calcular_promedio(lista):
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    
    if n % 2 == 0:
        medio1 = lista_ordenada[n // 2]
        medio2 = lista_ordenada[n // 2 - 1]
        mediana = (medio1 + medio2) / 2
    else:
        mediana = lista_ordenada[n // 2]
    
    return mediana
        
numeros_random = []

for i in range(10):
    #genera numeros aleatorios entre 1 y 100
    numero = random.randint(1,100)
    numeros_random.append(numero)

promedio = calcular_promedio(numeros_random);
mediana = calcular_mediana(numeros_random)

print(f"la lista es: {numeros_random}")
print(f"el promedio de la lista es: {promedio}")
print(f"la mediana de la lista es: {mediana}")