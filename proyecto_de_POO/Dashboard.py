import os

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Crear un nuevo script',  # Opción para crear un nuevo script
        '3': 'Unidad 2/2.1. Programacion tradicional frente a POO/2.1-2. Ejemplo NO. 02 - POO.py',
        # Agrega más scripts según sea necesario
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            if eleccion == '2':
                crear_nuevo_script()
            else:
                ruta_script = os.path.join(ruta_base, opciones[eleccion])
                mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def crear_nuevo_script():
    nombre_script = input("Introduce el nombre del nuevo script (con .py): ")
    contenido = input("Introduce el contenido del script: ")
    with open(nombre_script, 'w') as archivo:
        archivo.write(contenido)
    print(f"Script {nombre_script} creado exitosamente.")

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

# Llamada a la función principal para mostrar el menú
mostrar_menu()
