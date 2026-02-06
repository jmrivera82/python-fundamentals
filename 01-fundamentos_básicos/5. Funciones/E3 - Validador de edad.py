# Función que reciba edad
# Retorne True si es >= 18
# False en caso contrario
# Prueba con varias edades

def verificar_edad(edad):
    if edad >=18:
        return print(True)
    elif edad >=0 and edad <18:
        return print(False)
    else:
        return print("La edad no puede ser negativa")
    
verificar_edad(-5)
verificar_edad(1)
verificar_edad(20)