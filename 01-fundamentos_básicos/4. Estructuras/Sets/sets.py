s = {1, 2, 3, 3, 4, 5}
print(s) #{1, 2, 3, 4, 5} valores únicos

s = {1, 2, 3}
s.add(4)
print(s) #{1, 2, 3, 4}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2) #{3} -- unión

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2) #{1,2,3,4,5}

s1 = {1, 2, 3}
s2 = {2, 3}
print(s1 - s2) #{1}

s = {1, 2, 3}
s.remove(2)
print(s) #{1,3}

lista = [1, 2, 2, 3, 3, 3, 4]
s = set(lista) #conversión set-lista
print(len(s)) #4

s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1 & s2) # set()

s = {1, 2, 3}
s.discard(10) #{1,2,3}
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 ^ s2) #{1,4}