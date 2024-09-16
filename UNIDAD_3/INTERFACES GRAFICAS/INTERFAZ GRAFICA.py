import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación GUI")

# Crear los componentes
etiqueta = tk.Label(ventana, text="Ingrese un texto:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

lista = tk.Listbox(ventana)
lista.pack()

def agregar_item():
    texto = entrada.get()
    lista.insert(tk.END, texto)
    entrada.delete(0, tk.END)

def limpiar_lista():
    lista.delete(0, tk.END)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)
boton_agregar.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Iniciar el bucle principal
ventana.mainloop()