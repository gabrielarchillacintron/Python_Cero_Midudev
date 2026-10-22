>[!NOTE]
>Curso de Python desde cero de Midudev <br>
>[Youtube](https://www.youtube.com/@midudev) | [Video](https://youtu.be/TkN2i-_4N4g) | [Clase](https://midu.dev/curso/python-desde-cero/)
# Índice
* [Introducción](#Introducción)
* [Datos y Variables](#Datos-y-Variables)
    * [Módulos](#Módulos)
    * [Tipos](#Tipos)
        *[Casting de tipos](#Casting-de-tipos)
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
* `print()` es una función incorporada en Python que se utiliza para mostrar información en la consola o terminal. Permite imprimir texto, números, variables y otros tipos de datos. <br>
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

## Tipos
En python existen varios tipos de datos, entre ellos: int, float, str, bool, list, tuple, set, dict, complex, bytes, bytearray, memoryview, range y frozenset. <br>
- `int()`: números enteros, positivos o negativos. <br>
Python representa los números enteros con precisión arbitraria, lo que significa que no hay un límite superior para el tamaño de los enteros. <br>
- `float()`: números decimales, positivos o negativos. <br>
Aqui tambien podemos ver casos como `print(type(1e3))` que nos devuelve `<class 'float'>` ya que `1e3` es una notación científica que representa el número 1000.0. <br>
- `str()`: cadenas de texto, se pueden definir con comillas simples o dobles. <br>
- `bool()`: valores booleanos, True o False.
- `complex()`: números complejos, se representan con la letra `j` para la parte imaginaria. <br>
- `nonetype()`: `None` es un tipo de dato especial que representa la ausencia de valor o un valor nulo. <br>
No existe un tipo de dato `null` en Python, pero `None` cumple una función similar. <br>

La función `type()` permite conocer el tipo de dato de una variable. <br>
Ejemplo:
```python
print(type(10)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type("Hola")) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(1+2j)) # <class 'complex'>
print(type(None)) # <class 'NoneType'>
```
Aqui tambien puedes ver los comentarios de una sola linea con el simbolo `#` y los comentarios multilínea con tres comillas simples o dobles. <br>
Ejemplo:
```python  
    # Una sola linea
    '''
    Comentario multilínea
    '''
    """
    Comentario multilínea
    """
```

### Casting de tipos
Es la conversión de un tipo de dato a otro. <br>
Python no realiza la conversion automática de tipos, por lo que es necesario realizar el casting de tipos de manera explícita. <br>
Ejemplo:
```python
print(type(int("10"))) # <class 'int'>
print(int("10") + 5) # 15
```
Como poedemos ver en el ejemplo anterior, con el casting podemos interactuar con diferentes tipos de datos y realizar operaciones entre ellos. <br>
En el caso de cambiar un float a int, se pierde la parte decimal lo que afrecta la precisión. <br>
Ejemplo:
```python
print(int(3.14)) # 3
```
>[!WARNING]
>Importante: No redondea el número, simplemente elimina la parte decimal.

Para redondear un número decimal a su entero más cercano, se puede utilizar la función `round()`. <br>
Ejemplo:
```python
print(round(3.14)) # 3
print(round(3.5)) # 4
```
>[!NOTE]
>Pero hay casos extraños, como `print(round(2.5))` que nos devuelve `2` y `print(round(3.5))` que nos devuelve `4`.
>Esto se debe a que Python utiliza el método de redondeo "round half to even" o "redondeo al par más cercano", que redondea los números a su entero más cercano, y en caso de estar exactamente a la mitad, redondea al número par más cercano.
>Por lo que el par mas cercano a `2.5` es `2`, mientras que el par más cercano a `3.5` es `4`.
>De esta forma se distribuye el redondeo de manera más equitativa y se evita un sesgo acumulativo en cálculos que involucren múltiples redondeos.

En el casso de numeros como booleanos, todos los valores distintos de cero se consideran `True`, mientras que el valor `0` se considera `False`. <br>
Ejemplo:
```python
print(bool(0)) # False
print(bool(1)) # True
print(bool(-1)) # True
```
En el caso de las cadenas de texto, una cadena vacía se considera `False`, mientras que cualquier otra cadena se considera `True`. <br>
Ejemplo:
```python
print(bool("")) # False
print(bool("Hola")) # True
``` 
