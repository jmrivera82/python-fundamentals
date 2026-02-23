x = 10
if x > 5:
    print("Mayor")

x = 3
if x > 5:
    print("Mayor")
else:
    print("Menor")

edad = 17
if edad >= 18:
    print("Adulto")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")


x = 10
if x > 5:
    if x < 15:
        print("Entre 5 y 15")


nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")

#Bucle FOR
for i in range(3):
    print(i)

for i in range(1, 4):
    print(i)

for i in range(0, 6, 2):
    print(i)

frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

texto = "Hola"
for letra in texto:
    print(letra)


#Bucle WHILE

x = 0
while x < 3:
    print(x)
    x += 1

x = 5
while x > 0:
    print(x)
    x -= 1

x = 0
while x < 5:
    x += 1
    if x == 3:
        break
    print(x)

x = 0
while x < 3:
    x += 1
    if x == 2:
        continue
    print(x)

x = 0
while True:
    print(x)
    x += 1
    if x == 2:
        break


#Patrones

"""
#1: Acumulador
suma = 0
for i in range(1, 11):
    suma += i
print(suma)  # 55

#2: Contador
contador = 0
for letra in "hola":
    if letra in "aeiou":
        contador += 1
print(contador)  # 2

#3: Búsqueda
encontrado = False
for num in [1, 3, 5, 7]:
    if num == 5:
        encontrado = True
        break
print(encontrado)  # True

#4: Validación
while True:
    edad = int(input("Edad: "))
    if 0 < edad < 120:
        break
    print("Edad inválida")

    
#5: Menú
while True:
    print("1. Opción 1")
    print("2. Salir")
    
    opcion = input("Elige: ")
    
    if opcion == "1":
        # hacer algo
        pass
    elif opcion == "2":
        break
    else:
        print("Opción inválida")

"""