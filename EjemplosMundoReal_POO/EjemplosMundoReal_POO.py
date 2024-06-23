
# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def describir(self):
        return f'{self.anio} {self.marca} {self.modelo} de color {self.color}'

# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, color, puertas):
        super().__init__(marca, modelo, anio, color)
        self.puertas = puertas

    def describir(self):
        return f'{super().describir()} con {self.puertas} puertas'

# Clase Motocicleta que hereda de Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, color, tipo):
        super().__init__(marca, modelo, anio, color)
        self.tipo = tipo

    def describir(self):
        return f'{super().describir()} del tipo {self.tipo}'

# Clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, color, capacidad_carga):
        super().__init__(marca, modelo, anio, color)
        self.capacidad_carga = capacidad_carga

    def describir(self):
        return f'{super().describir()} con una capacidad de carga de {self.capacidad_carga} toneladas'

# Función principal para demostrar la interacción entre objetos
def main():
    # Crear instancias de diferentes tipos de vehículos
    coche = Coche("Toyota", "Corolla", 2020, "rojo", 4)
    motocicleta = Motocicleta("Yamaha", "Mt 09", 2022, "negro", "Ninja")
    camion = Camion("Hino", "GH", 2021, "blanco", 18)

    # Describir cada vehículo
    print(coche.describir())
    print(motocicleta.describir())
    print(camion.describir())

if __name__ == "__main__":
    main()
