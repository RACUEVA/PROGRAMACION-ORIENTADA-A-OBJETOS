class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, dia, temperatura):
        if 1 <= dia <= 7:
            self.temperaturas.append(temperatura)
        else:
            raise ValueError("El día debe estar entre 1 y 7.")

    def calcular_promedio(self):
        if len(self.temperaturas) == 7:
            return sum(self.temperaturas) / len(self.temperaturas)
        else:
            raise ValueError("Debe haber exactamente 7 temperaturas para calcular el promedio.")

def main():
    clima_semanal = ClimaSemanal()
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura para el día {i + 1}: "))
        clima_semanal.ingresar_temperatura(i + 1, temperatura)
    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

if __name__ == "__main__":
    main()
