# Leyes de De Morgan:
# not (A and B) = (not A) or (not B)
# not (A or B) = (not A) and (not B)

a = True
b = False

# Verifica la primera ley:
resultado1 = not (a and b)
resultado2 = (not a) or (not b)
print(f"¿Son iguales? {resultado1 == resultado2}")

# Verifica la segunda ley:
resultado3 = not (a or b)
resultado4 = (not a) and (not b)
print(f"¿Son iguales? {resultado3 == resultado4}")

