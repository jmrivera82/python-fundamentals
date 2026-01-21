"""
# Crea lista con números del 1 al 20
# Crea NUEVA lista solo con números divisibles por 3
# NO uses list comprehension, usa for y append
# Imprime la nueva lista

# ESCRIBE TU CÓDIGO AQUÍ:
# """

lista=[]
lista2=[] #creo una lista vacía
i=1

while True: #lleno la lista mientras no se cumpla detención 
    lista.append(i)
    i+=1

    if i>20:
        break

for num in lista: #recorro y agrego los multiplos de 3 a la nueva lista
    if num %3==0:
        lista2.append(num)

print(lista2)
