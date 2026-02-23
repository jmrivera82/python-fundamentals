# Dada: [1, 2, 3, 4, 5]
# Rota 2 posiciones a la derecha
# Resultado: [4, 5, 1, 2, 3]

lista=[1, 2, 3, 4, 5]

lista_nueva=lista[:] #copia nueva de lista para hacer los cambios

valor_lista=len(lista)
k=2 #constante de movimientos de rotación

for i in range(valor_lista):
    lista_nueva[(i+k)% valor_lista] = lista [i]
    print(i,lista_nueva) #Agrego print para analizar los cambios de posición de acuerdo al indice

print("Resultados")
print(lista)
print(lista_nueva)
