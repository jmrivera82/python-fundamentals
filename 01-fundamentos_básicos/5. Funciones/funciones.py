def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Ana")) #Hola Ana

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado) #8

def multiplicar(x, y):
    x * y

print(multiplicar(4, 5)) #None, no hay return

def contar():
    print("1")
    print("2")
    return "3"
    print("4")

contar() #imprime 1 y 2, retorna 3 y el print 4 queda fuera

def cambiar_valor(x):
    x = 100
    
a = 10
cambiar_valor(a)
print(a) #10 porque el valor de a no cambia

### Variación para verificar otros resultados

def cambiar_valor(a):
    a = 100
    
a = 10
cambiar_valor(a)
print(a) #imprime 10 ya que no hay return


def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5, 10)) #50

def es_par(n):
    return n % 2 == 0

print(es_par(7)) #False

def saludar(nombre="Mundo"):
    return f"Hola {nombre}"

print(saludar()) #Hola mundo porque el argumento está implicito

def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

x, y = calcular(10, 3)
print(x) #10

global_var = 100

def modificar():
    global_var = 200
    return global_var

modificar()
print(global_var) #100 porque en la función no se imprime su modificación