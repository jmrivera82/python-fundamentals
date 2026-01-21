"""# Crea una lista: [5, 2, 8, 2, 9, 2, 3, 2]
# Cuenta cuántas veces aparece el 2
# Encuentra la posición (índice) del primer 8
# Imprime ambos resultados

# ESCRIBE TU CÓDIGO AQUÍ:"""

lista=[5, 2, 8, 2, 9, 2, 3, 2]
cuenta1=lista.count(2) #cuento cuantas veces está el valor 2
cuenta2=lista.index(8) #encuentro el primer index del valor 8

print(f'El numero 2 se encuentra: {cuenta1} ocasiones')
print(f'El numero 8 se encuentra en la posición: {cuenta2}')



"""output
**Resultado esperado:** 

El 2 aparece 4 veces
El 8 está en la posición 2
"""