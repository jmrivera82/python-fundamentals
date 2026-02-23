# Dada: [0, 1, 0, 3, 12, 0, 5]
# Mueve todos los ceros al final manteniendo orden de los demás
# Resultado: [1, 3, 12, 5, 0, 0, 0]

lista=[0, 1, 0, 3, 12, 0, 5]
aux=len(lista)

print(lista)

for i, valor in enumerate(lista):

    if valor==0:
            lista.remove(lista[i])
            lista.append(valor)


print(lista)