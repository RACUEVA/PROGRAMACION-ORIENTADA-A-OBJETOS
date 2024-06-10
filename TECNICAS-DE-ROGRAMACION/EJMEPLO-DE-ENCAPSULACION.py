class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Encapsulamos la edad

    def obtener_edad(self):
        return self.__edad

    def establecer_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

# Uso de la clase Estudiante con encapsulación
estudiante2 = Estudiante("Ana", 22)
print(f"Edad de {estudiante2.nombre}: {estudiante2.obtener_edad()}")
estudiante2.establecer_edad(25)
print(f"Nueva edad de {estudiante2.nombre}: {estudiante2.obtener_edad()}")
