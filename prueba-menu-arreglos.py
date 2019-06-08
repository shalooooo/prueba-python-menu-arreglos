# se importa libreria numpy y se asigna el alias 'np'
import numpy as np

# se importa libreria os
import os

# se define funcion para limpiar la pantalla de la consola
def limpiar():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#variable que guardara la cantidad maxima de productos
cantidad_maxima_productos = 2

# se inicializa un arreglo para el nombre de los productos 
arreglo_nombre_producto = np.empty(cantidad_maxima_productos,dtype='U50')

# se inicializa un arreglo para el precio de los productos
arreglo_precio_producto = np.zeros(cantidad_maxima_productos)

# se inicializa variable para la opcion del menu
opcion = 0

# se inicializa variable para el indice de los arreglos
indice = 0

# menu principal
while opcion != 2:
    limpiar()
    print("####### MENU #######")
    print("Seleccione una opcion")
    print("1.- Agregar producto")
    print("2.- Realiza venta y salir")
    print("####################")
    # se pregunta al usuario su opcion deseada
    opcion = int(input())
    # agregar producto
    if opcion == 1:
        limpiar()
        if indice < cantidad_maxima_productos:
            # menu ingreso de producto
            print("Seleccione el producto a vender")
            print("1.- Lapiz - $390")
            print("2.- Cuaderno - $1990")
            print("3.- Goma - $300")
            producto_seleccionado = int(input())
            limpiar()
            if producto_seleccionado == 1:
                # lapiz
                arreglo_nombre_producto[indice] = 'Lapiz'
                arreglo_precio_producto[indice] = 390
                indice+=1
            elif producto_seleccionado == 2:
                # cuaderno
                arreglo_nombre_producto[indice] = 'Cuaderno'
                arreglo_precio_producto[indice] = 1990
                indice+=1
            elif producto_seleccionado == 3:
                # goma
                arreglo_nombre_producto[indice] = 'Goma'
                arreglo_precio_producto[indice] = 300
                indice+=1
            else:
                print("Seleccione una opcion valida")
        else:
            print("Ya no puede agregar mas productos")
            os.system("Pause")
    # realizar venta y salir
    elif opcion == 2:
        limpiar()
        # se inicializa acumulador del total a pagar de la venta
        total_venta = 0
        print("##########################################")
        print("############      Boleta      ############")
        print("##########################################")
        if indice > 0:
            # se muestra resumen
            for i in range(0, cantidad_maxima_productos):
                print(arreglo_nombre_producto[i] + " - $" + str(arreglo_precio_producto[i]))
                total_venta+=arreglo_precio_producto[i]
        print("##########################################")
        print("Total a pagar: $" + str(total_venta))
        print("##########################################")
        os.system("Pause")
    else:
        limpiar()
        print("Favor ingrese una opcion valida.")
        os.system("Pause")

