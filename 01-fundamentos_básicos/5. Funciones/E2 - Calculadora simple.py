# Crea 4 funciones: sumar, restar, multiplicar, dividir
# Cada una recibe dos números
# Retorna el resultado
# Prueba todas

def sumar(a,b):
    return print(f"{a} + {b} es: {a+b}")

def restar (a,b):
    return print(f"{a} - {b} es: {a-b}")

def multiplicar(a,b):
    return print(f"{a} * {b} es: {a*b}")


def dividir(a,b):
    if b!=0:
        return print(f"{a} / {b} es: {round(a/b)}")
    else:
        return print("No se puede dividir por 0")


a=10
b=0

sumar(a,b)
restar(a,b)
multiplicar(a,b)
dividir(a,b)
