"""
python# Dada tupla: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Usa desempaquetado para:
# primero = 1
# ultimo = 10
# resto = (2, 3, 4, 5, 6, 7, 8, 9)
# """

tupla=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
primero=tupla[0]
ultimo=tupla[-1]
resto=tupla[1:-1]

print(primero)
print(ultimo)
print(resto)