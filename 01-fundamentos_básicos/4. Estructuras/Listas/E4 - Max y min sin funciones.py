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

print("++Lista Original++")
print(lista)

for i in lista:
    for j in lista[:i+1:-1]: #recorro la lista de fin al comienzo sin incluir la primera posición
        if i>j:
            mayor=i
        elif i<j:
            menor=i

print(f'El número mayor es: {mayor}')
print(f'El número menor es: {menor}')

#print("++Lista ordenada++")

#print(lista)
    