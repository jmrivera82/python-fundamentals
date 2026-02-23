"""# Dada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Multiplica por 2 los números pares
# Deja los impares como están
# Modifica la lista original (no crees nueva)
# Imprime resultado"""

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0,len(lista)):

    if lista[i]%2==0: #revisión del elemento si tiene resto 0 es par
        lista[i]=lista[i]*2

print(lista)