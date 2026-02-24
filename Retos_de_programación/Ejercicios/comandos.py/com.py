#import random
#print(len(dir(random)))
"""
print("c",end='')
import a
import b

print(__name__)

"""
"""
try:
    raise Exception("Ocurrió un error")
except ValueError as ve:
    print("ValueError:", str(ve))
except BaseException as be:
    print("BaseException:", str(be))
except:
    print("Capturada alguna otra excepción")

#output: baseException

"""

"""
try:
    raise Exception("Se ha producido un error")
except Exception:
    print("a")
except:
    print("b")
except BaseException: #error de sintaxis
    print("c")


var=4
assert var >0
#error de assert cuando es negativo

x=r"\\\"
print(len(x))
#error literal


x="\\//"
print(len(x))
#esto imprime 3

print(chr(ord('a')+1))
#con el 1 imprime b


print(int("1.0"))
#valueError debe pasarse a flotante


class Class:
    def __init__(self, val=0):
        pass

#object=Class(1)
#object=Class(None)
#object=Class()
#object=Class(1,2) #INVALIDO

class CustomNumber:
    def __init__(self, value=1.5):
        self.value = value

    def increment(self, increase=2):
        self.value -= increase
        return self.value


num_instance = CustomNumber()
num_alias = num_instance
num_alias.increment()

print(num_instance.value)
#output -0.5

class A:
    A = 1
    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))

#false

class A:
    def __init__(self, v):
        self.__a = v + 1

class B(A):
    def __init__(self, v):
        super().__init__(v)
        self.__a += 1

b = B(0)
print(b._A__a)

#attributeError
"""

"""
class A:
    
    def __init__(self):
        pass

a=A(1)
print(hasattr(a, 'A'))
"""
"""
class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(B, A):
    def c(self):
        self.a()


o = C()
o.c()
#b

try:
    raise Exception(1, 2, 3, (4), "A",)
except Exception as e:
        print(len(e.args))

#5

def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in my_fun(2):
    print(x, end='')




class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')

def generate_pattern(n):
    def create_pattern():
        return '**' * n

    return create_pattern

pattern1 = generate_pattern(1) 
pattern2 = generate_pattern(2) 
print(pattern1() + pattern2()) 


"""


numbers = [0, 2, 7, 9, 10]
# Inserta la línea de código aquí.
foo=map(lambda num:num**2, numbers)
print(list(foo))

numbers2=[i*i for i in range(5)]
foo1=list(filter(lambda x:x%2,numbers))
foo2=list(map(lambda x:x//2, numbers))
foo3=list(filter(lambda x:x/2, numbers))

foo4=list(map(lambda x:x%2, numbers))
print(foo1)
print(foo2)
print(foo3)
print(foo4)

import os
print(os.uname())

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

