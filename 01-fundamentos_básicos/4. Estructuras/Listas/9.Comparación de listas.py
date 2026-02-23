"""# Dadas:
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [4, 5, 6, 7, 8]
# Encuentra elementos que están en AMBAS listas
# Imprime el resultado"""


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

for i in lista1:
    valor=lista1[i-1] #asigno el valor de lista a una variable

    for j in range(0,len(lista2)):
        if valor==lista2[j]: #comparo e imprimo
            print(valor) #Puedo crear una lista de resultados

