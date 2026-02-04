# Dada: [10, 20, 30, 20, 40, 20, 50]
# Encuentra el índice de la SEGUNDA aparición del 20
# Resultado: 3

lista= [10, 20, 30, 20, 40, 20, 50]
cont, buscar=0, 20
val=len(lista)

for i,valor in enumerate(lista): #si solo uso indice genero una tupla con indice y elemento

    if buscar==valor:
        cont+=1
        if cont >  1:
            print(f"el elemento {buscar} se repite en la posición {i}")
            break


#hacer que se revise una lista random