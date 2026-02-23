# Calcula IMC y determina categoría
# IMC = peso / altura²
# Bajo: < 18.5
# Normal: 18.5 - 24.9
# Sobrepeso: >= 25

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# ESCRIBE TU CÓDIGO:
imc = 0# Calcula IMC

# Determina categorías:
bajo_peso = 0# imc < 18.5
peso_normal = 0# 18.5 <= imc < 25
sobrepeso = 0# imc >= 25

print(f"IMC: {imc:.2f}")
print(f"Bajo peso: {bajo_peso}")
print(f"Peso normal: {peso_normal}")
print(f"Sobrepeso: {sobrepeso}")