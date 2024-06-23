# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(longitud, ancho):
    """
    Calcula el área de un rectángulo.

    Args:
        longitud (float): La longitud del rectángulo.
        ancho (float): El ancho del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    area = longitud * ancho
    return area


# Solicitar al usuario la longitud y el ancho del rectángulo
longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))

# Calcular el área del rectángulo
area_rectangulo = calcular_area_rectangulo(longitud, ancho)

# Mostrar el resultado
print(f"El área del rectángulo es: {area_rectangulo:.2f} unidades cuadradas")