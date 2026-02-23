"""
Crea un sistema que determine si una persona es elegible para un préstamo.

REQUISITOS PARA SER ELEGIBLE:
1. Edad entre 18 y 65 años
2. Ingresos mensuales >= $500
3. Tiene empleo estable (al menos 6 meses)
4. NO tiene deudas pendientes > $1000

El programa debe:
1. Pedir todos los datos
2. Calcular elegibilidad
3. Mostrar resultado detallado
4. Si es elegible, calcular monto máximo (3x ingresos mensuales)

Ejemplo de salida:
====================================
    EVALUACIÓN DE PRÉSTAMO
====================================
Nombre: Juan Pérez
Edad: 30 años ✓
Ingresos: $1200 ✓
Tiempo empleo: 24 meses ✓
Deudas: $500 ✓
------------------------------------
RESULTADO: ELEGIBLE ✓
Monto máximo: $3600
====================================
"""

# ESCRIBE TU CÓDIGO AQUÍ:



























"""

print("=" * 40)
print("    EVALUACIÓN DE PRÉSTAMO")
print("=" * 40)

# Solicitar datos
nombre = input("Nombre completo: ")
edad = int(input("Edad: "))
ingresos = float(input("Ingresos mensuales: $"))
meses_empleo = int(input("Meses en empleo actual: "))
deudas = float(input("Deudas pendientes: $"))

# Verificar condiciones
edad_ok = # TU CÓDIGO
ingresos_ok = # TU CÓDIGO
empleo_ok = # TU CÓDIGO
deudas_ok = # TU CÓDIGO

# Determinar elegibilidad
es_elegible = # TU CÓDIGO

# Calcular monto máximo
monto_maximo = # TU CÓDIGO (solo si es elegible)

# Mostrar resultados
print()
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años {'✓' if edad_ok else '✗'}")
print(f"Ingresos: ${ingresos} {'✓' if ingresos_ok else '✗'}")
print(f"Tiempo empleo: {meses_empleo} meses {'✓' if empleo_ok else '✗'}")
print(f"Deudas: ${deudas} {'✓' if deudas_ok else '✗'}")
print("-" * 40)

if es_elegible:
    print(f"RESULTADO: ELEGIBLE ✓")
    print(f"Monto máximo: ${monto_maximo}")
else:
    print(f"RESULTADO: NO ELEGIBLE ✗")

print("=" * 40)

"""