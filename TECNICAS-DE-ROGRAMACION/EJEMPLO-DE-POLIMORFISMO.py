class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)
        self.curso = curso

    def saludar(self):  # Polimorfismo
        return f"Hola, soy {self.nombre} y estudio en el curso de {self.curso}"

class Profesor(Persona):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia

    def saludar(self):  # Polimorfismo
        return f"Hola, soy el profesor {self.nombre} y enseño {self.materia}"

# Uso del polimorfismo
persona1 = Persona("Carlos")
estudiante4 = Estudiante("Laura", "Física")
profesor1 = Profesor("Juan", "Matemáticas")

print(persona1.saludar())     # Saludo de una persona
print(estudiante4.saludar())  # Saludo de un estudiante
print(profesor1.saludar())    # Saludo de un profesor
