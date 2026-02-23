x = 5
print(x)

nombre = "Juan"
edad = 25
print(nombre, edad)

a = 10
b = a
a = 20
print(b)

x = 5
x = x + 1
print(x)

mensaje = "Hola"
mensaje = "Chao"
print(mensaje)

x = 10
print(type(x))

y = 3.14
print(type(y))

a = 5
b = 2
print(a / b)
print(type(a / b))

x = 10
y = 3
print(x // y)  # División entera

x = 10
y = 3
print(x % y)  # Módulo (resto)

texto = "Python"
print(type(texto))

nombre = "Ana"
apellido = "Pérez"
completo = nombre + " " + apellido
print(completo)


palabra = "Hola"
print(palabra * 3)

texto = "Python"
print(texto[0])
print(texto[-1])

mensaje = "Hola Mundo"
print(len(mensaje))

#Tipos de datos

x = True
print(type(x))


a = 5
b = 10
resultado = a > b
print(resultado)

x = True
y = False
print(x and y)

x = True
y = False
print(x or y)

x = True
print(not x)

x = "10"
y = int(x)
print(type(y))

x = 10
y = str(x)
print(type(y))

x = "5"
y = "10"
print(x + y)

x = "5"
y = "10"
print(int(x) + int(y))

x = 3.7
y = int(x)
print(y)


# Asignación
x = 10

# Múltiple
a, b, c = 1, 2, 3

# Intercambio
a, b = b, a

int     # Entero: 10, -5, 0
float   # Decimal: 3.14, -2.5
str     # Texto: "hola", 'mundo'
bool    # Lógico: True, False

int("10")      # String → Int
str(10)        # Int → String
float("3.14")  # String → Float
int(3.7)       # Float → Int (trunca)

