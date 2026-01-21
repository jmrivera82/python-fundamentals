"""# Dada la lista: [1, 2, 3, 4, 5]
# Inviértela SIN usar reverse() o [::-1]
# Usa un bucle for
# Imprime la lista invertida"""

#[ 1 | 2 | 3 | 4 | 5 ]
#  ↑               ↑
#  i               j

lista=[1, 2, 3, 4, 5,6,7,8]
print(lista)        

i=0
j=len(lista)-1

while True:
    lista[i],lista[j]=lista[j],lista[i]
    i+=1
    j-=1
    if i>j:
        break

print(lista)        