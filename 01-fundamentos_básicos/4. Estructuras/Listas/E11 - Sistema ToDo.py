"""
Proyecto: Sistema de To-Do List básico
Requisitos:

Lista vacía al inicio
Menú con opciones:

1: Agregar tarea
2: Ver todas las tareas
3: Eliminar tarea (por índice)
4: Contar tareas
5: Salir
Validar que el usuario ingrese opción válida
Funcionar en bucle hasta que elija salir
"""

print("=====Sistema ToDo 1.0=====")
print("""
1: Agregar tarea
2: Ver todas las tareas
3: Eliminar tarea (por índice)
4: Contar tareas
5: Salir
      """)

mis_tareas=[]
cont=0 #contador de ingresos erroneos

while True:
    opcion=int(input(f"Ingrese Opción: "))

    if opcion ==1:
       
        tarea=input(f"Ingrese nombre de la tarea: ")
        mis_tareas.append(tarea)
        print(f"Tarea agregada!")

    elif opcion ==2:
        print(f"Lista de Tareas")
        for i, tarea in enumerate(mis_tareas):
            print(f'N°{i+1} - {tarea}')
    elif opcion ==3:
        continue
    elif opcion ==4:
        continue
    elif opcion ==5:
        print("Saliendo del programa..")
        break

    else:
        cont+=1
        if cont ==3:
            print("Exceso de ingresos no válidos, saliendo del programa..")
            break

        print("Opcion no válida, intente nuevamente")
