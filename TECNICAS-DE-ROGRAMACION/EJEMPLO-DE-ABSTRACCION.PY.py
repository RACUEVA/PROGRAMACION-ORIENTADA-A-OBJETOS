class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Uso de la clase Estudiante
estudiante1 = Estudiante("Juan", 20)
estudiante1.mostrar_informacion()
