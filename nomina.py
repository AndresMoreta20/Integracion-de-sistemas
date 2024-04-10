import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import csv

# Conectar a la base de datos SQLite
conn = sqlite3.connect('empleados.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
               (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, departamento TEXT)''')
conn.commit()

# Función para insertar un empleado en la base de datos
def guardar_empleado():
    cursor.execute("INSERT INTO empleados (nombre, apellido, departamento) VALUES (?, ?, ?)",
                   (nombre_var.get(), apellido_var.get(), departamento_var.get()))
    conn.commit()
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    departamento_entry.delete(0, tk.END)
    messagebox.showinfo("Guardado", "Empleado guardado con éxito")

# Función para exportar datos a CSV
def exportar_csv():
    # Consulta para obtener todos los datos de empleados
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()

    # Abrir (o crear si no existe) un archivo CSV para escribir los datos
    with open('empleados.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nombre', 'Apellido', 'Departamento'])  # Escribir el encabezado
        writer.writerows(empleados)  # Escribir los datos de los empleados

    messagebox.showinfo("Exportado", "Datos exportados a empleados.csv con éxito")

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Registro de Empleados")

# Variables para almacenar los inputs
nombre_var = tk.StringVar()
apellido_var = tk.StringVar()
departamento_var = tk.StringVar()

# Crear y colocar los campos de entrada
tk.Label(root, text="Nombre").grid(row=0, column=0)
nombre_entry = tk.Entry(root, textvariable=nombre_var)
nombre_entry.grid(row=0, column=1)

tk.Label(root, text="Apellido").grid(row=1, column=0)
apellido_entry = tk.Entry(root, textvariable=apellido_var)
apellido_entry.grid(row=1, column=1)

tk.Label(root, text="Departamento").grid(row=2, column=0)
departamento_entry = tk.Entry(root, textvariable=departamento_var)
departamento_entry.grid(row=2, column=1)

# Botón para guardar empleado
guardar_btn = ttk.Button(root, text="Guardar", command=guardar_empleado)
guardar_btn.grid(row=3, column=0)

# Botón para exportar a CSV
exportar_csv_btn = ttk.Button(root, text="Exportar CSV", command=exportar_csv)
exportar_csv_btn.grid(row=3, column=1)

# Ejecutar la ventana
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conn.close()
