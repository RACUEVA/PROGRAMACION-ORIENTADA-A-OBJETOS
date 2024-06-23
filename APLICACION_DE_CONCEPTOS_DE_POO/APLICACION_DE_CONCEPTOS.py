# Clase base: Vehículo
class Vehicle:
    def __init__(self, make, model, year):
        self._make = make    #atributo encapsulado
        self._model = model  #atributo encapsulado
        self._year = year    #atributo encapsulado

    def start(self):
        print(f"Encendiendo el {self._make} {self._model} del año {self._year}.")

    def stop(self):
        print(f"Apagando el {self._make} {self._model} del año {self._year}.")

# Clase derivada: Automóvil
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self._num_doors = num_doors

    def open_doors(self):
        print(f"Abriendo las {self._num_doors} puertas del {self._make} {self._model}.")

    def close_doors(self):
        print(f"Cerrando las {self._num_doors} puertas del {self._make} {self._model}.")

# Ejemplo de polimorfismo
def drive_vehicle(vehicle, speed):
    vehicle.start()
    print(f"Conduciendo el vehículo a {speed} km/h.")
    vehicle.stop()

# Crear instancias de las clases
my_car = Car("Toyota", "Corolla", 2020, 4)
my_motorcycle = Vehicle("Honda", "CBR600RR", 2018)

# Demostrar la funcionalidad
my_car.open_doors()
my_car.close_doors()
drive_vehicle(my_car, 80)
drive_vehicle(my_motorcycle, 120)
