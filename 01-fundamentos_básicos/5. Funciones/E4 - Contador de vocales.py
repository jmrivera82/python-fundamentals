# Función que reciba string
# Retorne cantidad de vocales (a,e,i,o,u)
# Prueba: "programacion" → 5

def contar_vocales(string):
    vocales=['a','e','i','o','u']
    cont=0

    for letra in string:
        if letra in vocales:
            print(f"se encontró la letra {letra}")
            cont+=1
        

    return print(f"{string} tiene {cont} vocales")


string="Programacion"
contar_vocales(string)