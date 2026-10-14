#Lista
list_productos = []

#Menu
menu = ("1. Agregar producto", 
        "2. Mostrar productos", 
        "3. Buscar producto", 
        "4. Eliminar producto", 
        "5. Salir")

#Recorrido del menu
while True:
    for opcion in menu:
        print(opcion)
    #seleccion del usuario
    seleccion = input("Seleccione una opción: ")

    #agregar productos
    if seleccion == "1":
        producto_nombre = input("Ingrese el nombre del producto: ").strip()
        while producto_nombre == "":
            print("El nombre del producto no puede estar vacío.")
            producto_nombre = input("Ingrese el nombre del producto: ").strip()

        producto_categoria  = input("Ingrese la categoría del producto: ").strip()
        while producto_categoria == "":
            print("La categoría del producto no puede estar vacía.")
            producto_categoria  = input("Ingrese la categoría del producto: ").strip()

        producto_precio = input("Ingrese el precio del producto: ").strip()
        while not producto_precio.isdigit() or int(producto_precio) <= 0:
            print("El precio del producto debe ser un número positivo.")
            producto_precio = input("Ingrese el precio del producto: ").strip()

        producto_precio = int(producto_precio)
        list_productos.append([producto_nombre, producto_categoria, producto_precio])
        print(f"Producto '{producto_nombre}' agregado.")
    #Mostrar productos
    elif seleccion == "2":
        if list_productos:
            print("Productos en la lista:")
            for i, (nombre, categoria, precio) in enumerate(list_productos, start=1):
                print(f" {i}. {nombre}: ${precio} (Categoría: {categoria})")
        else:
            print("No hay productos en la lista.")
    #Buscar productos
    elif seleccion == "3":
        producto_nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        encontrado = False
        while producto_nombre == "":
            print("El nombre del producto no puede estar vacío.")
            producto_nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        for nombre, categoria, precio in list_productos:
            if producto_nombre.lower() in nombre.lower():
                print(f"Producto encontrado: {nombre}: ${precio} (Categoría: {categoria})")
                encontrado = True   
                
        if not encontrado :
            print(f"Producto '{producto_nombre}' no encontrado.")
    #Eliminar productos
    elif seleccion == "4":
        if list_productos:
            print("Productos en la lista:")
            for i, (nombre, categoria, precio) in enumerate(list_productos, start=1):
                print(f" {i}. {nombre}: ${precio} (Categoría: {categoria})")

            numero = input("Ingrese el número del producto a eliminar: ").strip()
            while not numero.isdigit() or int(numero) < 1 or int(numero) > len(list_productos):
                print(f"Debe ingresar un número entre 1 y {len(list_productos)}.")
                numero = input("Ingrese el número del producto a eliminar: ").strip()

            
            posicion = int(numero) - 1
            producto_eliminado = list_productos.pop(posicion)
            print(f"Producto '{producto_eliminado[0]}' eliminado.")
        else:
            print("No hay productos en la lista.")
    #salir
    elif seleccion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")