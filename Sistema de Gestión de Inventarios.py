class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificar si el ID ya existe
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("El ID ya existe.")
            return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print(f"Producto '{p.get_nombre()}' eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id, nuevo_nombre=None, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if nuevo_nombre:
                    p.set_nombre(nuevo_nombre)
                if nueva_cantidad:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio:
                    p.set_precio(nuevo_precio)
                print(f"Producto '{p.get_nombre()}' actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def buscar_productos_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("No hay productos en el inventario.")


def menu():
    inventario = Inventario()
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)
        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para omitir): ")
            nueva_cantidad = input("Ingrese la nueva cantidad (o presione Enter para omitir): ")
            nuevo_precio = input("Ingrese el nuevo precio (o presione Enter para omitir): ")
            inventario.actualizar_producto(id, nuevo_nombre if nuevo_nombre else None,
                                           int(nueva_cantidad) if nueva_cantidad else None,
                                           float(nuevo_precio) if nuevo_precio else None)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_productos_por_nombre(nombre)
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()