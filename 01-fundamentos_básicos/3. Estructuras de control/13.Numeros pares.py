# Imprime solo números pares del 0 al 20

# ESCRIBE TU CÓDIGO AQUÍ:

numero = 20
cont=0
for i in range(0,numero+1):
    if i %2==0:
        print(f'numero: {i}')
        cont+=1

print(f'Se imprimieron: {cont} números')