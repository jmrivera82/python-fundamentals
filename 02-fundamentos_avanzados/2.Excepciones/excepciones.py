try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")

try:
    x = int("abc")
except ValueError:
    print("No es número")


try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("Índice inválido")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Éxito")

try:
    x = 10 / 0
except:
    print("Algo falló")
finally:
    print("Siempre ejecuto")

def dividir(a, b):
    if b == 0:
        raise ValueError("No dividir por cero")
    return a / b

try:
    dividir(10, 0)
except ValueError as e:
    print(e)

try:
    x = int("123")
except ValueError:
    print("Error")
else:
    print("OK")
finally:
    print("Fin")

try:
    d = {'a': 1}
    print(d['b'])
except KeyError:
    print("Clave no existe")


try:
    x = 10 / 2
    y = int("abc")
except ZeroDivisionError:
    print("División")
except ValueError:
    print("Valor")


try:
    archivo = open("noexiste.txt")
except FileNotFoundError:
    print("Archivo no encontrado")

###############Avanzado###################

class MiError(Exception):
    pass

try:
    raise MiError("Algo salió mal")
except MiError as e:
    print(e)


try:
    x = int("10")
except ValueError:
    print("Error")
except Exception:
    print("Otro error")
else:
    print("Todo bien")


def procesar():
    try:
        return "resultado"
    finally:
        print("Limpieza")

print(procesar())


try:
    raise ValueError("Error 1")
except ValueError:
    raise TypeError("Error 2")
except TypeError:
    print("Capturado")


class EdadInvalida(Exception):
    def __init__(self, edad):
        self.edad = edad
        super().__init__(f"Edad {edad} inválida")

try:
    raise EdadInvalida(150)
except EdadInvalida as e:
    print(e.edad)


