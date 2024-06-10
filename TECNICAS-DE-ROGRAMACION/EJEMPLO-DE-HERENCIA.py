class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Estudiante(Persona):  # Hereda de Persona
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.curso = curso

    def mostrar_informacion(self):  # Sobrescribe el método de Persona
        super().mostrar_informacion()
        print(f"Curso: {self.curso}")

# Uso de la clase Estudiante con herencia
estudiante3 = Estudiante("María", 21, "Matemáticas")
estudiante3.mostrar_informacion()
