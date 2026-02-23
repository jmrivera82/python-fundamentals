# Dada: [[1, 2], [3, 4], [5, 6]]
# Crea lista plana: [1, 2, 3, 4, 5, 6]

matriz=[[1, 2], [3, 4], [5, 6]]
lista_plana=[] #para listar por fila
lista_plana2=[] #para listar por columna

filas=len(matriz)
columnas=len(matriz[0])

#indice i es la fila
#indice j es la columna

for i in range(filas):
    for j in range(columnas):
        lista_plana.append(matriz[i][j])
    
print("=====Matriz inicial 3 x 2=====")
print(matriz)
print("=====Lista plana resultante=====")
print(lista_plana)

#Si invierto el ciclo obtengo otra lista plana [1,3,5,2,4,6], ojo con los indices
for j in range(columnas):
    for i in range(filas):
        lista_plana2.append(matriz[i][j])
    
print("=====Matriz inicial 3 x 2=====")
print(matriz)
print("=====Lista plana resultante=====")
print(lista_plana2)
