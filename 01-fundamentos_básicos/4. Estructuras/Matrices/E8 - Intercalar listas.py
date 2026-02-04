# Dadas:
# lista1 = [1, 3, 5]
# lista2 = [2, 4, 6]
# Intercala: [1, 2, 3, 4, 5, 6]

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
intercalada=[]

for i, valor in enumerate(lista1):
    
    intercalada.append(valor)
    intercalada.append(lista2[i])

print(intercalada)