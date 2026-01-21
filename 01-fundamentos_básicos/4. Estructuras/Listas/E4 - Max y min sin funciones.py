"""
# Dada la lista: [23, 67, 12, 89, 45, 34, 91, 56]
# Encuentra el máximo SIN usar max()
# Encuentra el mínimo SIN usar min()
# Imprime ambos

# ESCRIBE TU CÓDIGO AQUÍ:
```

**Resultado esperado:**
```
Máximo: 91
Mínimo: 12
"""

lista=[23, 67, 12, 89, 45, 34, 91, 56]
mayor=lista[0]
menor=lista[0]

print("++Lista Original++")
print(lista)

for num in lista:
    if num > mayor:
        mayor=num

    elif num < menor:
        menor=num

print(f'El número mayor es: {mayor}')
print(f'El número menor es: {menor}')


    