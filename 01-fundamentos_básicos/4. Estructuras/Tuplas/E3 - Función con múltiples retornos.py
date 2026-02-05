"""
# Crea función que reciba lista de números
# Retorne (mínimo, máximo, promedio) como tupla
# Prueba con: [5, 10, 15, 20, 25]
"""


def tupla(lista):
    
    min=lista[0]
    max=lista[0]

    for num in lista:
        if num > max:
            max=num

        elif num < min:
            min=num


    prom=sum(lista)/len(lista)
    tup=(min,max,prom)
    print(type(tup))

    return print(tup)


#prom, min, max=0,0,0
lista=[5, 10, 15, 20, 25]
tupla(lista)


