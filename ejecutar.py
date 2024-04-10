import subprocess
import time

def ejecutar_script_node():
    try:
        # Ejecutar el script de Node.js
        resultado = subprocess.run(['node', 'receptor.js'], check=True, text=True, capture_output=True)
        print(f"Script ejecutado con éxito:\n{resultado.stdout}")
    except subprocess.CalledProcessError as e:
        # Manejo de error si el script de Node.js falla
        print(f"Error al ejecutar script:\n{e.stderr}")

def ejecucion_periodica(intervalo=5):
    try:
        while True:
            print("Ejecutando el script de Node.js...")
            ejecutar_script_node()
            time.sleep(intervalo)  # Esperar 5 segundos antes de la próxima ejecución
    except KeyboardInterrupt:
        # Permite detener el programa con Ctrl+C
        print("Detenido por el usuario.")

if __name__ == "__main__":
    ejecucion_periodica()
