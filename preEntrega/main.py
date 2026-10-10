from funciones import *

listaProductos = []

while True:
    print("¡BIENVENIDO AL MENU!")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir del menu")

    opcionElegida = input("Seleccione una opción: ") 

    if(opcionElegida == "1"):
        ingresarDatosProductos(listaProductos)
    elif(opcionElegida == "2"):
        mostrarProductos(listaProductos)
    elif(opcionElegida == "3"):
        buscarProducto(listaProductos)
    elif(opcionElegida == "4"):
        eliminarProducto(listaProductos)
    elif(opcionElegida == "5"):
        print("Saliendo del menu...")
        break
    else:
        print("Opción invalida. Intente nuevamente")

