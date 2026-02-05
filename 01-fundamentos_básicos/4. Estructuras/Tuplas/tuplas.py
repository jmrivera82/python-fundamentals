tupla = (1, 2, 3, 4, 5)
print(tupla[2]) #3

t = (10, 20, 30)
#t[0] = 100
#error, la tupla es inmutable

tupla = (1, 2, 2, 3, 2, 4)
print(tupla.count(2))
#3

t = ('a', 'b', 'c', 'd')
print(t.index('c'))
#devuelve el index del elemento 'c': 2

a, b, c = (10, 20, 30)
print(b)
#20

tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
nueva_tupla = tuple(lista)
print(nueva_tupla)
#(1,2,3,4) -- conversiones lista / tupla

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)
#forma una lista (1,2,3,4)

tupla = (5,)
print(type(tupla)) #class tuple
print(len(tupla)) #1

coordenadas = [(1, 2), (3, 4), (5, 6)]
print(coordenadas[1][0])
#3

def obtener_datos():
    return (100, 200, 300)

x, y, z = obtener_datos()
print(y)
#200
