from scripts.planilla_asistencia import generar_planilla

import tkinter as tk
from tkinter import messagebox
import webbrowser

def generar_interfaz():
    def enviar_datos():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        mes = entry_mes.get().capitalize()
        tipo_documento = entry_tipo_documento.get()
        if tipo_documento == "Planilla de Asistencia":
            generar_planilla(dni, nombre, mes)
            messagebox.showinfo("Éxito", "Planilla generada correctamente")
        # Agrega más condiciones para otros tipos de documentos aquí

    def mostrar_formulario(*args):
        global entry_dni, entry_nombre, entry_mes
        tipo_documento = entry_tipo_documento.get()
        for widget in frame_formulario.winfo_children():
            widget.destroy()
        if tipo_documento == "Planilla de Asistencia":
            tk.Label(frame_formulario, text="DNI:").grid(row=0, column=0, padx=10, pady=5)
            entry_dni = tk.Entry(frame_formulario)
            entry_dni.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(frame_formulario, text="Nombre Completo:").grid(row=1, column=0, padx=10, pady=5)
            entry_nombre = tk.Entry(frame_formulario)
            entry_nombre.grid(row=1, column=1, padx=10, pady=5)

            tk.Label(frame_formulario, text="Mes (en español):").grid(row=2, column=0, padx=10, pady=5)
            meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            entry_mes = tk.StringVar(frame_formulario)
            entry_mes.set(meses[0])  # set the default value
            tk.OptionMenu(frame_formulario, entry_mes, *meses).grid(row=2, column=1, padx=10, pady=5)

            tk.Button(frame_formulario, text="Generar Documento", command=enviar_datos).grid(row=3, columnspan=2, pady=10)
        else:
            frame_formulario.pack_forget()

    def abrir_github():
        webbrowser.open_new("https://github.com/lostdou")

    root = tk.Tk()
    root.title("Generador de Documentos")
    root.geometry("600x400")
    root.resizable(False, False)

    tk.Label(root, text="Tipo de Documento:").pack(pady=5)
    tipos_documento = ["Planilla de Asistencia", "Otro Documento"]
    entry_tipo_documento = tk.StringVar(root)
    entry_tipo_documento.set(tipos_documento[0])  # set the default value
    tk.OptionMenu(root, entry_tipo_documento, *tipos_documento).pack(pady=5)
    entry_tipo_documento.trace("w", mostrar_formulario)

    frame_formulario = tk.Frame(root)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame_formulario, text="DNI:").grid(row=0, column=0, padx=10, pady=5)
    entry_dni = tk.Entry(frame_formulario)
    entry_dni.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_formulario, text="Nombre Completo:").grid(row=1, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(frame_formulario)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_formulario, text="Mes (en español):").grid(row=2, column=0, padx=10, pady=5)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    entry_mes = tk.StringVar(frame_formulario)
    entry_mes.set(meses[0])  # set the default value
    tk.OptionMenu(frame_formulario, entry_mes, *meses).grid(row=2, column=1, padx=10, pady=5)

    tk.Button(frame_formulario, text="Generar Documento", command=enviar_datos).grid(row=3, columnspan=2, pady=10)

    # Añadir el footer
    frame_footer = tk.Frame(root)
    frame_footer.pack(side="bottom", fill="x", padx=10, pady=10)

    tk.Label(frame_footer, text="V 1.0").pack(side="left")
    tk.Label(frame_footer, text="© 2025 Creado por lostdou").pack(side="left", expand=True)

    github_icon = tk.PhotoImage(file=r"assets\github.png").subsample(20, 20)
    github_button = tk.Button(frame_footer, image=github_icon, command=abrir_github)
    github_button.pack(side="right")

    root.mainloop()

generar_interfaz()