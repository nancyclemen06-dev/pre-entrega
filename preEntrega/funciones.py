
def ingresarDatosProductos(carrito):
    nombre = input("Ingrese el nombre del producto: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacio")
        nombre = input("Ingrese el nombre del producto: ").strip()
           
    categoria = input("Ingrese la categoria del producto: ").strip()
    while categoria == "":
        print("La categoria no puede estar vacia")
        categoria = input("Ingrese la categoria del producto: ").strip()

    precio = input("Ingrese el precio del producto: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("El precio debe ser un número mayor a 0")
        precio = input("Ingrese el precio del producto: ")

    subLista = [nombre, categoria, int(precio)]
    carrito.append(subLista)

    print(f"El producto {nombre} ha sido agregado al carrito correctamente")
    

def mostrarProductos(lista):
    if len(lista) == 0:
        print("No hay productos agregados")
    else:
        for i in range(len(lista)):
            producto = lista[i]
            print(f"{i + 1}. Producto: {producto[0]} | Categoria: {producto[1]} | Precio: ${producto[2]}")

def buscarProducto(lista):
    producto = input("Ingrese un producto: ")
    for prod in lista:
        if(producto.lower() == prod[0].lower()):
            print(prod)
        else:
            print("No se encontraron resultados")

def eliminarProducto(lista):
    print(lista)
    posicion = (input("Ingrese posición del producto a eliminar: "))
    if(len(lista) == 0):
        print("No hay elementos que eliminar")
    if(not posicion.isdigit()):
        print("Debe escribir un número")
    posicion2 = int(posicion) - 1
    lista.pop(posicion2)
    print(f"Se ha eliminado el producto {posicion2 + 1} satisfactoriamente")