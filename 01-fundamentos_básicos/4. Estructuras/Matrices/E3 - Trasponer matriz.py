# Dada:
# [[1, 2, 3],
#  [4, 5, 6]]
# Crea la transpuesta:
# [[1, 4],
#  [2, 5],
#  [3, 6]]

matriz=[1, 2, 3],[4, 5, 6]
matriz_nueva=[]

filas=len(matriz)
columnas=len(matriz[0])

#indice i es la fila
#indice j es la columna

for j in range(columnas):
    fila_nueva=[] #Agrego una fila vacía por cada iteración de columna
    for i in range(filas):
            fila_nueva.append(matriz[i][j])
    matriz_nueva.append(fila_nueva) #agrego la fila nueva a la matriz nueva
    
print("=====Matriz inicial 3 x 2=====")
print(matriz)
print("=====Matriz Resultante 2 x 3=====")
print(matriz_nueva)