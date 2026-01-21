"""
# Crea una lista con los números del 1 al 10
# Elimina los números 3, 6 y 9
# Agrega el número 100 al final
# Imprime la lista resultante

# ESCRIBE TU CÓDIGO AQUÍ:
# """


lista=[] #creo una lista vacía
i=1

while True: #lleno la lista mientras no se cumpla detención 
    lista.append(i)
    i+=1

    if i>10:
        break

for num in lista: #recorro y elimino los multiplos de 3
    if num %3==0:
        lista.remove(num)

lista.append(100) #agrego el 100 al final
print(lista)

#Resultado esperado: [1, 2, 4, 5, 7, 8, 10, 100]