import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import re  # Importar el módulo re para expresiones regulares


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Crear un frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # Crear TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("fecha", "hora", "descripcion"), show='headings')
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack()

        # Crear un frame para la entrada de datos
        self.frame_entry = ttk.Frame(self.root)
        self.frame_entry.pack(pady=10)

        # Campos de entrada
        ttk.Label(self.frame_entry, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entry)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entry, text="Hora (HH:MM):").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entry)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entry, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = tk.Entry(self.frame_entry)
        self.descripcion_entry.grid(row=2, column=1)

        # Botones de acción
        ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento).pack(pady=5)
        ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(pady=5)
        ttk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def validar_hora(self, hora):
        """Valida que la hora esté en formato HH:MM."""
        pattern = r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'
        return re.match(pattern, hora) is not None

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            if not self.validar_hora(hora):
                messagebox.showwarning("Advertencia", "La hora debe estar en formato HH:MM.")
                return

            # Agregar el evento a la lista
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpiar campos después de agregar el evento
            self.fecha_entry.delete(0, 'end')
            self.hora_entry.delete(0, 'end')
            self.descripcion_entry.delete(0, 'end')
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmation = messagebox.askyesno("Confirmar eliminación",
                                               "¿Está seguro de que desea eliminar este evento?")
            if confirmation:
                for item in selected_item:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()