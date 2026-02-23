# Una contraseña es válida si:
# - Tiene 8 caracteres o más
# - Contiene números
# - NO es igual a "password123"

password = input("Contraseña: ")

longitud_ok = len(password) >= 8
tiene_numero = any(c.isdigit() for c in password)  # Esto lo verás después
no_es_debil = password != "password123"

es_valida = longitud_ok and tiene_numero and no_es_debil

print(f"Longitud OK: {longitud_ok}")
print(f"Tiene número: {tiene_numero}")
print(f"No es débil: {no_es_debil}")
print(f"¿Es válida? {es_valida}")