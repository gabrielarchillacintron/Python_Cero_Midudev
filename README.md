>[!NOTE]
>Curso de Python desde cero de Midudev <br>
>[Youtube](https://www.youtube.com/@midudev) | [Video](https://youtu.be/TkN2i-_4N4g) | [Clase](https://midu.dev/curso/python-desde-cero/)
# Índice
* [Introducción](#Introducción)
* [Datos y Variables](#Datos-y-Variables)
    * [Módulos](#Módulos)
___
# Introducción
Creador: Guido van Rossum

- Año: 1991

Ventajas:
- Intuitivo
- Codigo Abierto
- Comprensible
- Rapido

Es un lenguaje interpretado, de alto nivel; no necesita compilación y esta mas cerca del lenguaje humano. Es un lenguaje de proposito general, multiparadigma y multiplataforma. Posee una biblioteca estandar muy amplia y una gran comunidad de desarrolladores. El nombre de Python proviene de la serie de comedia británica Monty Python's Flying Circus.

Desventajas:
- Lento
- No desarrollado para aplicaciones moviles
- Consumo de memoria elevado
- Global Interpreter Lock (GIL): inconveninte para aplicaciones multihilo, ya que solo permite la ejecución de un hilo a la vez y aplicaciones de procesamiento paralelo, lo que puede limitar el rendimiento en tareas que requieren un alto grado de paralelismo.

Editores de código recomendados por Midudev:
- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python Sandbox](https://pythonsandbox.io/editor)

Python tiene interprete interactivo, lo que permite ejecutar código línea por línea y ver los resultados de inmediato. Esto facilita la experimentación y prueba de fragmentos de código sin necesidad de crear un archivo completo. <br>
En el terminal: `python3`

Extensiones:
- Python
- Pylance
- Python Debugger

# Datos y Variables
Los nombres de los archivos normalmente se hacen en minúsculas y separados por guiones bajos. Al final de los nombres de los archivos se coloca la extensión `.py`. <br>
Ejemplo: `mi_archivo.py`

## Módulos
Los módulos son archivos de Python que contienen definiciones y declaraciones de funciones, clases y variables.
* print() es una función incorporada en Python que se utiliza para mostrar información en la consola o terminal. Permite imprimir texto, números, variables y otros tipos de datos. <br>
Ejemplo: `print("Hola, Mundo!")` <br>
Igual se pueden imprimir multiples elementos separados por comas. <br>
Ejemplo: `print("Hola", "Mundo!")` <br>
El separador por defecto es un espacio, pero se puede cambiar con el argumento `sep`. <br>
Ejemplo: `print("Hola", "Mundo!", sep="-")` <br>
También se puede imprimir en la misma línea utilizando el argumento `end`. <br>
Ejemplo:
```python
print("Hola", end=" ")
print("Mundo!")
```


