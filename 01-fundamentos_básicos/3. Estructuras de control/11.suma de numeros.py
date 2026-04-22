# Suma números del 1 al 100

suma = 0

# ESCRIBE TU CÓDIGO AQUÍ:

numero = int(input('Ingrese numero para calcular su suma: '))
print(f'****'*10)
print(f'Se imprimirán la suma del 1 al numero: {numero}')
i=1

for i in range(1,numero+1):
    suma +=i
    #print(suma)


print(f"Suma: {suma}")

