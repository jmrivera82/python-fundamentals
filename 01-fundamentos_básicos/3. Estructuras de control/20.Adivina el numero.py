# Número secreto: 7
# Usuario tiene 3 intentos

numero_secreto = 7
intentos = 0
max_intentos = 3

# ESCRIBE TU CÓDIGO AQUÍ:

print(f"Adivina el número secreto")

while True:
    numero=int(input("Ingresa un numero: "))
   
    intentos+=1
    if numero==numero_secreto:
        if intentos ==1:
            print(f'Excelente, adivinaste el número al primer intento ')
            break
        else:
            print(f'Excelente, adivinaste el número en {intentos} intentos')
            break
    print(f'Número equivocado')
    if intentos == 3:
        print(f'Se acabaron tus intentos')
        break