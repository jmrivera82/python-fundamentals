# Misma matriz del ejercicio anterior
# Calcula la suma de cada columna
# Imprime: Columna 0: 12, Columna 1: 15, Columna 2: 18

matriz=[1, 2, 3],[4, 5, 6],[7, 8, 9]
suma=0 #acumulador de suma

filas=len(matriz)
columnas=len(matriz[0])

#indice i es la fila
#indice j es la columna

for j in range(columnas):
    for i in range(filas):
        suma+=matriz[i][j]

    print(f"Columna {j}: {suma}")
    suma=0 #Se vuelve a inicializar en 0 para sumar otra columna