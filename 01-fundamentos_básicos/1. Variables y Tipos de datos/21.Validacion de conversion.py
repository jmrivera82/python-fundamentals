# Pide número al usuario
# Intenta convertir a int
# Si falla, muestra error

#entrada = int(input("Ingresa un número: "))

#print(int(entrada))

#Probar try-except

try:
    entrada = int(input("Ingresa un número: "))
    print(entrada)

except  ValueError:
    print("Debe ingresar un número")

