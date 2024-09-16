import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
app = tk.Tk()
app.title('Mi primera Aplicación GUI Básica')
app.geometry('500x500')

# Establecer el fondo gris de la ventana
app.config(bg='gray')

# Función para agregar texto a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Etiqueta para indicar el campo de texto
label = tk.Label(app, text="Ingrese un dato:", font=('Arial', 12))
label.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(app, font=('Arial', 12))
entrada_texto.pack(pady=10)

# Botón para agregar datos
btn_agregar = tk.Button(app, text="Agregar", command=agregar_dato, bg='blue', fg='white', font=('Arial', 10, 'bold'))
btn_agregar.pack(pady=10)

# Lista para mostrar los datos
lista_datos = tk.Listbox(app, font=('Arial', 12), width=40, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
btn_limpiar = tk.Button(app, text="Limpiar", command=limpiar_lista, bg='red', fg='white', font=('Arial', 10, 'bold'))
btn_limpiar.pack(pady=10)

# Ejecutar la ventana principal
app.mainloop()
