# Determina si un número es par o impar
# Usa el operador % (módulo)

numero = int(input("Número: "))

if numero%2==0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")