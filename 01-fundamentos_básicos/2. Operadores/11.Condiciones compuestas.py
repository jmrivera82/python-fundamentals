# Sistema de acceso

edad = int(input("Edad: "))
tiene_permiso = input("¿Tiene permiso? (s/n): ").lower() == 's'

# Puede entrar si:
# - Tiene 18 años o más Y tiene permiso
# - O tiene permiso de un adulto (representado por tiene_permiso)

puede_entrar = (edad >= 18 and tiene_permiso)

print(f"¿Puede entrar? {puede_entrar}")

