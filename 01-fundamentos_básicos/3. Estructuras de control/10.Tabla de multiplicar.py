# Imprime tabla del 5 (5x1 hasta 5x10)

numero = 5

# ESCRIBE TU CÓDIGO AQUÍ:

numero = int(input('Ingrese numero para calcular su tabla: '))
print(f'****'*50)
print(f'Se imprimirán la tabla del numero: {numero}')
i=1
for i in range(i,13):
    resultado=numero*i
    print(f'{numero} x {i} = {resultado}')