

# Función que calcule factorial
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Usa bucle, no recursión

def factorial_con_while (numero):
    resultado=numero
    i=numero-1
    
    while True:

        resultado*=i
        i-=1

        if i==1:
            break

    return print(f"El factorial de {numero} es: {resultado}")


def factorial_con_for (numero):

    resultado=1

    for i in range(numero, 0, -1):
        resultado*=i
        
    return print(f"El factorial de {numero} es: {resultado}")


numero=3
factorial_con_while(numero)
factorial_con_for(numero)