
# Gestión de Empleados con Exportación e Importación de Datos

Este proyecto ofrece una solución completa para la gestión de datos de empleados, utilizando un script de Python para la captura y almacenamiento de datos en una base de datos SQLite, con la capacidad de exportar estos datos a un archivo CSV. Posteriormente, un script de Node.js permite importar estos datos desde el archivo CSV a una base de datos NeDB, almacenándolos en un formato optimizado.

![image](https://github.com/AndresMoreta20/Integracion-de-sistemas/assets/61909582/315ff623-7a11-466f-9520-9f697afe54fc)



## Características

- Captura de datos de empleados mediante una interfaz gráfica de usuario (GUI) en Python.
- Almacenamiento de datos en una base de datos SQLite.
- Exportación de los datos de empleados a un archivo CSV.
- Importación de datos desde un archivo CSV a una base de datos NeDB utilizando Node.js.

## Requisitos Previos

Antes de iniciar, asegúrate de tener instalado Python y Node.js en tu sistema. También necesitarás `pip` para Python y `npm` para Node.js para instalar las dependencias.

Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
Node.js: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

## Instalación

Primero, clona este repositorio a tu máquina local:

```
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### Para el script de Python:

Instala las dependencias necesarias ejecutando:

```
pip install tkinter
```

Nota: `sqlite3` ya viene incluido con Python.

### Para el script de Node.js:

Instala las dependencias necesarias con:

```
npm install nedb csv-parser
```

## Uso

### Script de Python para gestión de empleados:

Para iniciar la interfaz de usuario y comenzar a gestionar los datos de empleados, ejecuta:

```
python script_python.py
```

Sigue las instrucciones en la GUI para añadir, guardar y exportar los datos de empleados.

### Script de Node.js para importar datos:

Una vez exportados los datos a un archivo CSV, puedes importarlos a NeDB con:

```
node script_node.js
```

## Contribución

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y crea un pull request con tus cambios. También puedes abrir un issue con la etiqueta "enhancement" para sugerencias de nuevas características o con la etiqueta "bug" si encuentras algún error.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
