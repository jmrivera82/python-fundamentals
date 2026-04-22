# Pide 3 números
# Determina cuál es el mayor


# ESCRIBE TU CÓDIGO AQUÍ:


a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

if a > b :
    if a > c:
        print(f'El numero mayor es :{a}')

    elif b > c:
        print(f'El numero mayor es :{b}')
        
    else:
        print(f'El numero mayor es :{c}')

else:
    if b > c:
        print(f'El numero mayor es :{b}')

    elif c > a:
        print(f'El numero mayor es :{c}')