frutas = ['manzana', 'pera', 'uva', 'kiwi']
print(frutas) #['manzana', 'pera', 'uva', 'kiwi']
print(frutas[1]) #pera

numeros = [1, 2, 3, 4, 5]
numeros.append(6) #agrega el 6 al final
print(len(numeros)) #devuelve la cantidad de items
print(numeros)
print(numeros[-1])

numeros.remove(4) #eliminará el valor 4 de la lista
print(numeros)

numeros.insert(3,4) #Agrega el valor 4 en la posición 3 (contando desde 0)
print(numeros)

print (numeros[1:4]) # Devuelve valores desde la posición 1 a la 3 (rebanar) 2,3,4

numeros2=numeros
numeros2.append(7) #Se copian las listas y ambas mutan
print(numeros)

numeros3 = [3, 1, 4, 1, 5, 9, 2]
numeros3.sort() #ordena el arreglo de menor a mayor
print(numeros3)

lista = ['a', 'b', 'c', 'd', 'e']
print(lista[::2]) #devuelve valores cada 2 saltos 'inicio:fin:salto'

x = [1, 2, 3]
y = x.pop() #Buscar explicacion --
print(x)
print(y)

lista = [1, 2, 3, 4, 5]
for i in lista:
    if i % 2 == 0: #Condición para extraer numeros pares en la lista
        print(i) 