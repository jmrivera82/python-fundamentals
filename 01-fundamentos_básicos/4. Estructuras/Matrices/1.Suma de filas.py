"""# Dada matriz:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Calcula la suma de cada fila
# Imprime: Fila 0: 6, Fila 1: 15, Fila 2: 24"""

matriz=[1, 2, 3],[4, 5, 6],[7, 8, 9]
suma=0 #acumulador de suma
i=0 #contador de filas

for fila in matriz: #iteración en cada fila
    i+=1
    for valor in fila: #ciclo para sumar los valores de la fila
        suma+=valor
    
    print(f"Fila {i}: {suma}")
    suma=0


#Otro ejemplo con una matriz diferente

matriz=[11, 22, 33],[14, 52, 88],[66,80,99]
suma=0 #acumulador de suma
i=0 #contador de filas

for fila in matriz: #iteración en cada fila
    i+=1
    for valor in fila: #ciclo para sumar los valores de la fila
        suma+=valor
    
    print(f"Fila {i}: {suma}")
    suma=0