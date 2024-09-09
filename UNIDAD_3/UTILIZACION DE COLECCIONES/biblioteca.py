# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {[libro.titulo for libro in self.libros_prestados]}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros (ISBN: Libro)
        self.usuarios = {}  # Diccionario para almacenar usuarios (ID: Usuario)
        self.historial_prestamos = []

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("El usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado de la biblioteca.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return
        if isbn not in self.libros:
            print("El libro no está disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.libros_prestados.append(libro)
        self.historial_prestamos.append((usuario, libro))
        del self.libros[isbn]
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_a_devolver = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)

        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros[isbn] = libro_a_devolver
            print(f"Libro '{libro_a_devolver.titulo}' devuelto por {usuario.nombre}.")
        else:
            print("El libro no fue prestado a este usuario.")

    def buscar_libros(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            match = True
            for clave, valor in kwargs.items():
                if not hasattr(libro, clave) or getattr(libro, clave).lower() != valor.lower():
                    match = False
                    break
            if match:
                resultados.append(libro)
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con los criterios.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("El usuario no está registrado.")


# Función para mostrar el menú interactivo
def mostrar_menu():
    print("\nSistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados a un usuario")
    print("9. Salir")


# Función principal
def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN (4 dígitos): ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID de usuario (único): ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo, autor, categoria): ")
            valor = input(f"Introduce el valor para {criterio}: ")
            biblioteca.buscar_libros(**{criterio: valor})

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            print("Saliendo del sistema de gestión de biblioteca.")
            break

        else:
            print("Opción no válida, por favor elige una opción del menú.")


if __name__ == "__main__":
    main()
