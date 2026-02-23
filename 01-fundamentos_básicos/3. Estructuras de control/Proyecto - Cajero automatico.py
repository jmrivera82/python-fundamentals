"""
Simula un cajero automático

MENÚ:
1. Consultar saldo
2. Depositar
3. Retirar
4. Salir

Reglas:
- Saldo inicial: $1000
- No permitir retiros mayores al saldo
- No permitir depósitos negativos
- Menú se repite hasta elegir salir
"""

# ESCRIBE TU CÓDIGO AQUÍ:

saldo = 1000

while True:
    print("\n" + "=" * 30)
    print("      CAJERO AUTOMÁTICO")
    print("=" * 30)
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    
    opcion = input("\nElige opción: ")
    
    # TU CÓDIGO AQUÍ