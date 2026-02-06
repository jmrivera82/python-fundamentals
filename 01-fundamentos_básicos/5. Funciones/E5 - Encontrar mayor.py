# Función que reciba lista de números
# Retorne el mayor SIN usar max()
# Prueba con [3, 7, 2, 9, 4]



def lista_de_numeros(lista):

    num=0

    for numero in lista:
        if num < numero:
            num=numero

    return print(f"El número mayor la lista es el {num}")



lista=[3, 7, 2, 9, 4]
print(lista)
lista_de_numeros(lista)