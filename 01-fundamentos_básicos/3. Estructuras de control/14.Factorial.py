# Calcula factorial de un número
# 5! = 5 * 4 * 3 * 2 * 1 = 120

numero = int(input("Número: "))
factorial = 1

# ESCRIBE TU CÓDIGO AQUÍ:

for i in range (numero,0,-1):
    factorial= factorial * i



print(f"{numero}! = {factorial}")

