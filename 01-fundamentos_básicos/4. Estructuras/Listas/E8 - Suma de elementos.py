"""
# Dada: [10, 20, 30, 40, 50]
# Calcula la suma SIN usar sum()
# Calcula el promedio
# Imprime ambos
# """

lista=[10, 20, 30, 40, 50]
suma=0

for i in lista:
    suma+=i         #sumo cada elemento 'i' de la lista

print(f'La suma es: {suma}')
print(f'El promedio es: {suma/len(lista)}')