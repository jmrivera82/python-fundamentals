import math
print(math.sqrt(16))

from math import pi
print(pi)


import random
random.seed(42)
print(random.randint(1, 10))

from math import sqrt as raiz
print(raiz(25))


import sys
print(type(sys.argv))

####

# archivo: mi_modulo.py
#def saludar():
#    return "Hola"

# archivo: main.py
#import mi_modulo
#print(mi_modulo.saludar())

#####

from datetime import datetime
now = datetime.now()
print(type(now))


import os
print(os.path.exists("archivo.txt"))


# ¿Qué hace este código?
if __name__ == "__main__":
    print("Ejecutando directamente")


import json
data = json.dumps({"nombre": "Ana"})
print(type(data))



###########################33

# Estructura:
# mi_paquete/
#   __init__.py
#   modulo1.py

# ¿Qué hace __init__.py?

# En __init__.py:
#from .modulo1 import funcion1

# ¿Qué hace el punto en .modulo1?