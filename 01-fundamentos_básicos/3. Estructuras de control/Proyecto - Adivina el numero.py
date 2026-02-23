"""
Juego de adivinar número

Reglas:
- Número aleatorio entre 1 y 100
- Usuario tiene 7 intentos
- Dar pistas: "mayor" o "menor"
- Contar intentos
- Opción de jugar de nuevo
"""

import random

# ESCRIBE TU CÓDIGO AQUÍ:

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

print("=" * 40)
print("  ADIVINA EL NÚMERO (1-100)")
print("=" * 40)

# TU CÓDIGO AQUÍ