texto = "Python es GENIAL"
print("=====1=====")
print(texto.lower())

texto = "   hola mundo   "
print("=====2=====")

print(texto.strip())

texto = "Python-es-genial"
print("=====3=====")

print(texto.split("-"))

palabras = ["Hola", "Mundo"]
print("=====4=====")
print(" ".join(palabras))

texto = "Python"
print("=====5=====")
print(texto[1:4])

texto = "banana"
print("=====6=====")
print(texto.count("a"))

texto = "Python es genial"
print("=====7=====")
print(texto.replace("genial", "increíble"))

texto = "12345"
print("=====8=====")

print(texto.isdigit())

texto = "Python"
print("=====9=====")

print(texto.startswith("Py"))

texto = "Hola Mundo"
print("=====10=====")

print(texto.find("Mundo"))


nombre = "Ana"
edad = 25
print(f"Hola {nombre}, tienes {edad} años")

precio = 1234.5678
print(f"${precio:.2f}")

num = 42
print(f"{num:05d}")

texto = "Python"
print(f"{texto:>10}")

a, b = 10, 20
print("a={}, b={}".format(a, b))

texto = "Hola\nMundo"
print(texto)

path = r"C:\Users\nombre"
print(path)

multilinea = """
Línea 1
Línea 2
"""
print(len(multilinea.split("\n")))

nombre = "Juan"
print("Hola %s" % nombre)

numero = 255
print(f"{numero:b}")  # binario



