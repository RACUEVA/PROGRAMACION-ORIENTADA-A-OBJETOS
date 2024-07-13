# tarea de constructor y destructor

class Mensaje:
    def __init__(self, texto):
        # CONSTRUCTOR inicia la tarea con un nombre
        self.texto = texto
        print(f"Tarea ´{self.texto}´ha sido creada.")

    def __del__(self):
        # DESTRUCTOR limpia o cierra la tarea
        print(f"Tarea '{self.texto}' está siendo destruida.")

# crear instancia
if __name__=="__main__":
    mensaje1 = Mensaje("Constructor y Desctructor")
    mensaje2 = Mensaje("Ejercicio")

    # destruir la tarea
del mensaje1

# El destructor de mensaje2 será llamado al final del programa