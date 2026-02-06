
persona = {'nombre': 'Ana', 'edad': 25}
print(persona['nombre']) #Ana


d = {'a': 1, 'b': 2}
d['c'] = 3 #Agrega otro par k:v
print(d) #{'a': 1, 'b': 2, 'c':3}

producto = {'nombre': 'Laptop', 'precio': 1000}
print(producto.get('stock', 0))# 0 

d = {'x': 10, 'y': 20, 'z': 30}
print(d.keys()) #{x,y,z}

d = {'a': 1, 'b': 2, 'c': 3}
print(d.values()) #{1,2,3}

d = {'nombre': 'Juan', 'edad': 30}
for clave, valor in d.items():
    print(clave, valor) #bucle para mostrar par de k:v

d = {'a': 1, 'b': 2}
d['a'] = 100
print(d) #{'a': 100, 'b': 2}

d = {'x': 10}
valor = d.pop('x')
print(d) #{}
print(valor) #10

d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d1.update(d2) #se fusionarán  y actualizará valor de 'b'
print(d1)

d = {'a': 1, 'b': 2, 'c': 3}
if 'b' in d:
    print(d['b']) #2