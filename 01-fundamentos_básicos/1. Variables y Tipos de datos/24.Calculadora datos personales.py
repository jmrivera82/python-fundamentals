"""
Crea un programa que:

1. Pida al usuario:
   - Nombre completo
   - Edad
   - Altura (en metros)
   - Peso (en kg)

2. Calcule:
   - IMC (peso / altura²)
   - Año de nacimiento (2024 - edad)
   - Si es mayor de edad (>= 18)

3. Muestre todo formateado bonito

Ejemplo de salida:
==========================================
       INFORMACIÓN PERSONAL
==========================================
Nombre: Juan Pérez
Edad: 25 años
Altura: 1.75 m
Peso: 70 kg
------------------------------------------
IMC: 22.86
Año de nacimiento: 1999
Mayor de edad: Sí
==========================================
"""

nombre=input("Ingrese su nombre")
edad=int(input("Ingrese su edad"))
altura=float(input("Ingrese su altura (en mts)"))
peso=float(input("Ingrese su peso"))

imc=float(peso/altura**2)

print("==========================================")
print(("INFORMACIÓN PERSONAL"))
print("==========================================")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"Peso: {peso}")
print("------------------------------------------")
print(f"IMC: {imc}")
print(f"Año de nacimiento {2026-edad}")
print(f"Mayor de edad: ")
print("==========================================")