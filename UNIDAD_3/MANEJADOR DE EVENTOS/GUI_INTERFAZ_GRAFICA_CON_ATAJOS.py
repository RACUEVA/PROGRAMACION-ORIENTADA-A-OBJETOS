import tkinter as tk
from tkinter import messagebox

# Funciones para manejar las tareas
def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

def marcar_completada(event=None):
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, f"{tarea} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

def eliminar_tarea(event=None):
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

def cerrar_app(event=None):
    ventana.quit()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")

# Campo de entrada de tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)  # Atajo para agregar tarea (Enter)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, height=10, width=40, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Botones de la interfaz
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar Completada", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Atajos de teclado
ventana.bind("<C>", marcar_completada)  # Atajo para marcar como completada (tecla C MAYUSCULA)
ventana.bind("<D>", eliminar_tarea)  # Atajo para eliminar tarea (tecla D MAYUSCULA)
ventana.bind("<Delete>", eliminar_tarea)  # Atajo adicional para eliminar tarea (tecla Delete)
ventana.bind("<Escape>", cerrar_app)  # Atajo para cerrar la aplicación (tecla Escape)

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()
