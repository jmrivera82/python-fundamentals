"""
Sistema para calcular calificaciones

Funcionalidades:
1. Ingresar nombre de estudiante
2. Ingresar 5 notas
3. Calcular promedio
4. Determinar si aprueba (>= 60)
5. Mostrar letra (A, B, C, D, F)
6. Preguntar si quiere ingresar otro estudiante
7. Al final, mostrar resumen de todos
"""

# ESCRIBE TU CÓDIGO AQUÍ:

estudiantes = []

while True:
    print("\n" + "=" * 40)
    print("   SISTEMA DE CALIFICACIONES")
    print("=" * 40)
    
    # TU CÓDIGO AQUÍ
    
    continuar = input("\n¿Otro estudiante? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostrar resumen
print("\n" + "=" * 40)
print("           RESUMEN")
print("=" * 40)

# TU CÓDIGO AQUÍ