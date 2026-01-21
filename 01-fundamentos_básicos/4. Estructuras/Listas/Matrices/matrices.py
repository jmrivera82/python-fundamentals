matriz = [[1, 2], [3, 4], [5, 6]]
print(matriz[1][0]) #3

lista = [1, 2, 3, 4, 5]
nueva = lista[1:4] #extrae el 2,3 y 4
nueva.append(10)
print(lista)
print(nueva)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b #[1,2,3,4,5,6]
print(c)

lista = ['a', 'b', 'c']
lista.insert(1, 'x') #a,x,b,c
print(lista)

numeros = [5, 2, 8, 1, 9]
print(numeros)
numeros.sort() #ordena de menor a mayor
print(numeros)
mayor = numeros[-1] #toma el último elemento que es el mayor
print(mayor)

lista = [10, 20, 30]
lista.extend([40, 50]) #extiende la lista con 40,50
print(lista)

lista = [1, 2, 3, 4, 5]
lista.reverse() #invierte el orden dejando el 5 como el indice 0
print(lista[0])

matriz = [[1, 2, 3], [4, 5, 6]]
for fila in matriz:
    print(fila[1])  #primera vuelta toma la fila [1,2,3] el indice 1 valor 2

lista = [1, 2, 2, 3, 3, 3, 4]
print(lista.count(3)) #cuenta cuantos 3 hay (3)

original = [1, 2, 3]
copia = original.copy() #copia el arreglo
copia.append(4) #Se agrega un 4 solo a la copia 
print(len(original))
print(len(copia))

original=copia #en este caso se copia el arreglo y se modifican ambos
copia.append(5)
print(len(original))
print(len(copia))

