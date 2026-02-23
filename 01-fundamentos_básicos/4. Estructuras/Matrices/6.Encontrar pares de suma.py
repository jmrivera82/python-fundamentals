# Dada lista: [1, 2, 3, 4, 5, 6]
# Encuentra todos los pares que suman 7
# Resultado: (1,6), (2,5), (3,4)

lista = [1, 2, 3, 4, 5, 6]
aux=0
largo_lista=len(lista)
resultado=[]

for i in lista:
    aux=i #guardo el valor de la iteracion para compararlo con el resto en una variable auxiliar
    for i in range(i+1,largo_lista+1): #inicio el bucle de comparación desde el segundo elemento
        if aux+i==7:
            par=(aux,i) #almaceno el par que suma 7 en una variable
            resultado.append(par) #agrego la variable a la lista resultado en forma de tupla
           
print(resultado)
