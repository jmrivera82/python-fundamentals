# Calcula promedio de números ingresados

numeros = [85, 90, 78, 92, 88]
suma = 0

# ESCRIBE TU CÓDIGO AQUÍ:

promedio=0

cantidad=len(numeros)
for i in numeros:
    suma+=i

promedio=suma/cantidad
print(f'La suma de la lista números [{numeros}] es = {suma}')
print(f"Promedio: {promedio}")

