# Pide números hasta que la suma sea >= 100

suma = 0
cont = 0

# ESCRIBE TU CÓDIGO AQUÍ:

while True:

    numero=int(input(f'Ingresa un número para ir sumando hasta que pase los 100: '))
    suma+=numero
    cont+=1
    if suma >=100:
        break

print(f"Suma final: {suma}")
print(f'Se sumaron {cont} números')

