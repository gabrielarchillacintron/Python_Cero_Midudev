>[!NOTE]
>Curso de Python desde cero de Midudev <br>
>[Youtube](https://www.youtube.com/@midudev) | [Video](https://youtu.be/TkN2i-_4N4g) | [Clase](https://midu.dev/curso/python-desde-cero/)
___
# Índice
* [Introducción](#introducción)
* [Datos y Variables](#datos-y-variables)
    * [Módulos](#módulos)
    * [Tipos](#tipos)
        * [Casting de tipos](#casting-de-tipos)
    * [Variables](#variables)
        * [Tipado de variables](#tipado-de-variables)
    * [Introduccion de datos input()](#introduccion-de-datos-input)
* [Condicionales](#condicionales)
    * [If, else y elif](#if-else-y-elif)
    * [Operadores Logicos](#operadores-logicos)
        * [Tabla de verdad: and](#tabla-de-verdad-and)
        * [Tabla de verdad: or](#tabla-de-verdad-or)
        * [Tabla de verdad: not](#tabla-de-verdad-not)
    * [Condicionales anidados](#condicionales-anidados)
    * [Booleanos](#booleanos)
        * [Operadores de comparación](#operadores-de-comparación)
    * [Operadores Ternarios](#operadores-ternarios)
* [Listas](#listas)
    * [Acceder a elementos de una lista](#acceder-a-elementos-de-una-lista)
    * [Slicing de listas](#slicing-de-listas)
    * [Modificar elementos de una lista](#modificar-elementos-de-una-lista)
    * [Agregar elementos a una lista](#agregar-elementos-a-una-lista)
    * [Métodos para listas](#métodos-para-listas)
* [Bucles Loops](#bucles-loops)
    * [While](#while)
        * [Try Except](#try-except)
    * [For](#for)
        * [For anidados](#for-anidados)
        * [Break y Continue](#break-y-continue)
        * [Comprensión de listas](#comprensión-de-listas-list-comprehension)
            * [Condición dentro de list comprehension](#condición-dentro-de-list-comprehension)
        * [Rango (range)](#rango-range)
   
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
* `import`: se utiliza para importar modulos de Python. <br>
Ejemplo: 
```python
import os
os.system("clear")
```
Esto es para limpiar la terminal.

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
## Variables
Las variables son contenedores que almacenan datos y permiten manipularlos a lo largo del programa. En Python, no es necesario declarar el tipo de dato de una variable, ya que se infiere automáticamente a partir del valor asignado. <br>
Estas son reasignables, lo que significa que se puede cambiar el valor de una variable en cualquier momento. <br>
### Tipado de variables
* `Tipado dinamico` : El tipo de dato se determina automáticamente en tiempo de ejecución según el valor asignado a la variable. <br>
Ejemplo:
```python
str_variable = "Hola"
print(type(str_variable)) # <class 'str'>
str_variable = 10
print(type(str_variable)) # <class 'int'>
```

* `Tipado fuerte`: no realiza la conversión automática de tipos, por lo que es necesario realizar el casting de tipos de manera explícita. <br>
Ejemplo:
```python
print(10 + "5") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10 + int("5")) # 15
```
* Cadenas literales formateadas `(f-strings)`: permiten incrustar expresiones dentro de cadenas de texto utilizando llaves `{}`. <br>
Ejemplo:
```python
name = "Alice"
age = 30
print(f"Me llamo {name} y tengo {age} años.") # Me llamo Alice y tengo 30 años.
```

>[!WARNING]
>No recomendado: `name, age, city = "Alice", 30, "New York"`.
>Ya que es menos legible y más propenso a errores, especialmente si se agregan o eliminan variables en el futuro.

Se recomienda el uso de `snake_case` para los nombres de variables, funciones y métodos, y `PascalCase` para los nombres de clases. <br>
Ejemplo:   
```python
class MyClass:
    def my_method(self):
        my_variable = 10
``` 
Python no tiene constantes, pero se puede simular su comportamiento utilizando variables con nombres en mayúsculas, el `UPPER_CASE`. <br>
Ejemplo:
```python
PI = 3.14159
```
Otros formatos no validos son:
```python
myVariable = 10 # camelCase
my-variable = 10 # kebab-case
123123_variable = 10 # invalid
my variable = 10 # invalid
```
Claro esta que Python posee variables reservadas, que no se pueden utilizar como nombres de variables, funciones o clases. <br>

En Python, el tipado de variables es dinámico y fuerte. Esto significa que el tipo de una variable se determina automáticamente en tiempo de ejecución según el valor que se le asigne, y no se permite la conversión implícita entre tipos de datos incompatibles. <br>
Ejemplo:
```python
variable = True # La variable es de tipo bool
variable = 42 # Ahora la variable es de tipo int
```
* `Tipado estatico`: En lenguajes de tipado estático, el tipo de una variable se determina en tiempo de compilación y no puede cambiar durante la ejecución del programa. <br>
Ejemplo:
```python
variable = "nombre"
variable = 42
variable = str = "palabra"
```
En este caso, `str` funciona como una documentación para indicar que la variable es de tipo cadena de texto, pero no impide que se le asigne un valor de otro tipo. <br>

## Introduccion de datos input()
Esta función permite al usuario introducir datos durante la ejecución del programa. <br>
Ejemplo:
```python
name = input("Introduce tu nombre:\n")
print(f"Hola, {name}!")
```
Estos tambien se puesden restringir a un tipo de dato específico, como `int` o `float`, utilizando el casting de tipos. <br>
Ejemplo:
```python
age = int(input("Introduce tu edad:\n"))
print(f"Tienes {age} años.")
```
De igual forma se puede introiducir mas de un dato a la vez, separandolos por comas. <br>
Ejemplo:
```python
name, age = input("Introduce tu nombre y edad:\n").split()
print(f"Hola, {name}! Tienes {age} años.")
```
En este caso se separan por espacios pero se puede escoger otro como `split(",")` para separar por comas.

# Condicionales
## If, else y elif
Ejecutar bolques de código basados en condiciones. <br>
Ejemplo:
```python
nota = int(input("Introduce tu not del 0 al 10:\n"))
if nota <= 5:
    print("F")
elif nota == 6:
    print("D")
elif nota == 7:
    print("C")
elif nota == 8:
    print("B")
elif nota == 9:
    print("A")
else:
    print("No calificado")
```
Aqui podemos ver bifurcaciones. 
>[!WARNING]
>Mientras menos difurcaciones, mejor; ya que puede ser dificil de leer y mantener.

## Operadores Logicos
* `and` : Ambos se tienen que cumplir.
* `or` : Uno de los dos se debe cumplir.
* `not` : Niega el valor de la condición.

### Tabla de verdad: and
| A | B | A and B |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |
### Tabla de verdad: or
| A | B | A or B |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |
### Tabla de verdad: not
| A | not B |
|---|---|
| T | F |
| F | T |

## Condicionales anidados
Los condicionales pueden estar dentro de otros para evaluar múltiples niveles de decisiones. <br>
Ejemplo:
```python
edad = 20
tiene_dinero = True
 
if edad >= 18:
   if tiene_dinero:
      print("Puedes ir a la discoteca")
   else:
      print("Quédate en casa")
else:
   print("No puedes entrar a la disco")
```

## Booleanos
### Operadores de comparación
Los operadores de comparación devuelven valores booleanos al evaluar relaciones entre valores y cadenas de texto. <br>
Ejemplo:
```python
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 3)   # True
print(5 >= 5)   # True
print(5 <= 3)   # False

print("manzana" < "pera") # True; Comparacion alfabetica letra por letra
print("Hola" == "hola") # False; sensible a mayusculas
```
Tambien pasa que una variable de tipo numero distinto de cero sera True en un caso de condicion booleana y en una cadena de texto no vacia tambien sera True. <br>
Ejemplo:
```python
numero = 5
if numero: # True 
numero = 0
if numero: # False
##########################
nombre = "Juan"
if nombre:
nombre = ""
if nombre:
```

## Operadores Ternarios
En Python, la condición ternaria es una forma compacta de escribir un if-else en una sola línea de código. Es ideal para simplificar el código cuando necesitas asignar un valor basado en una condición. <br>
`[valor_si_verdadero] if [condición] else [valor_si_falso]` <br>
Ejemplo:
```python
print("La condición ternaria:")
edad = 17 
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
```

# Listas
Conjunto de elementos. Se pueden modificar, agregar o eliminar elementos después de su creación. <br>
Ejemplo:
```python
lista = [1, 2, 3, 4, 5]
print(lista)
```
Estan pueden tener tipos ya que pueden contener elementos de diferentes tipos. <br>
Ejemplo:
```python
lista_mixta = [1, "Hola", 3.14, True]
print(lista_mixta)
```
De igual manera los puede identificar en ella. <br>
Ejemplo:
```python
lista = list(int | str | float | bool) = [1, "Hola", 3.14, True]
```
Se pueden tener listas vacias y una lista de listas. `lista = []`<br>
Asi mismo matrices pueden ser representadas como listas de listas. <br>
Ejemplo:
```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
```

## Acceder a elementos de una lista
Se puede acceder a los elementos de una lista utilizando índices. Los índices comienzan en 0. <br>
Ejemplo:
```python
lista = [10, 20, 30, 40, 50]
print(lista[0])  # 10
print(lista[2])  # 30
print(lista[-1]) # 50 (último elemento). Mientras incrementamos el índice desde el final, -1 es el último, -2 el penúltimo, y así sucesivamente.
```
En el case de acceder a un elemento que esta en una lista dentro de otra lista, se utilizan múltiples índices. <br>
Ejemplo:
```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0][1])  # 2 (primer fila, segundo elemento o columna)
print(matriz[2][0])  # 7 (tercera fila, primer elemento o columna)
```

## Slicing de listas
Se puede obtener una sublista utilizando la sintaxis de slicing. <br>
Sus parámetros son `[inicio:fin:paso]`. <br>
Ejemplo:
```python
lista = [10, 20, 30, 40, 50]
print(lista[1:4])  # [20, 30, 40] (sublista desde el índice 1 hasta el 3)
print(lista[:3])   # [10, 20, 30] (sublista desde el inicio hasta el índice 2)
print(lista[2:])   # [30, 40, 50] (sublista desde el índice 2 hasta el final)
print(lista[:])    # [10, 20, 30, 40, 50] (toda la lista)
print(lista[::2])  # [10, 30, 50] (sublista con paso 2)
print(lista[::3])  # [10, 40] (sublista con paso 3)
print(lista[::-1]) # [50, 40, 30, 20, 10] (sublista en orden inverso)
```
>[!WARNING]
>El el parametro `fin` no está incluido en el slicing.

>[!Note]
>Para saber la longitud de una lista se utiliza `len(lista)`

## Modificar elementos de una lista
Se pueden modificar elementos de una lista accediendo a ellos mediante su índice. <br>
Ejemplo:
```python
lista = [10, 20, 30, 40, 50]
lista[1] = 25
print(lista)  # [10, 25, 30, 40, 50]
```
## Agregar elementos a una lista
Se pueden agregar elementos a una lista utilizando los métodos `append()` y `extend()`. <br>
Ejemplo:
```python
lista = [10, 20, 30]
lista.append(40)  # Agrega un solo elemento al final de la lista
print(lista)  # [10, 20, 30, 40]

lista.extend([50, 60])  # Agrega múltiples elementos al final de la lista
print(lista)  # [10, 20, 30, 40, 50, 60]

lista = lista + [70, 80]  # Agrega múltiples elementos al final de la lista
print(lista)  # [10, 20, 30, 40, 50, 60, 70, 80]

lista += [90, 100]  # Agrega múltiples elementos al final de la lista
print(lista)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```
## Metodos para listas
* `append(elemento)`: Agrega un solo elemento al final de la lista.
* `extend(lista)`: Agrega múltiples elementos al final de la lista.
* `insert(indice, elemento)`: Inserta un elemento en la posición especificada.
* `remove(elemento)`: Elimina la primera aparición del elemento en la lista.
* `pop(indice)`: Elimina y devuelve el elemento en la posición especificada. Si no se especifica el índice, elimina y devuelve el último elemento.
* `index(elemento)`: Devuelve el índice de la primera aparición del elemento.
* `count(elemento)`: Devuelve el número de veces que aparece el elemento en la lista.
* `sort()`: Ordena la lista en orden ascendente. <br>
En el caso de texto, se puede utilizar el parámetro `key=str.lower` para ordenar sin diferenciar mayúsculas y minúsculas.
* `sorted(lista)`: Devuelve una nueva lista ordenada sin modificar la original.
* `reverse()`: Invierte el orden de los elementos en la lista.
* `clear()`: Elimina todos los elementos de la lista.
* `copy()`: Devuelve una copia superficial de la lista.
* `len(lista)`: Devuelve la cantidad de elementos en la lista de 1 a n.

>[!NOTE]
>Para eliminar un rango de elementos de una lista se puede utilizar slicing y la palabra clave `del`.
>
>Ejemplo:
>```python
>lista = [10, 20, 30, 40, 50]
>del lista[1:4]  # Elimina los elementos desde el índice 1 hasta el 3
>print(lista)  # [10, 50]
>```

>[!NOTE]
>Formas de copiar.
>```python
>original = [1, 2, 3] 
>copia_1 = original[::] # slicing
>copia_2 = original.copy()
>referncia = original # Si le haces un cambio a la referencia, se le aplicara a la original.
>```

# Bucles Loops
## While
Bloque de codigo repetitivo ientras se cumpla una condicion. <br>
Ejemplo:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
>![WARNING]
>Es importante incrementar para evitar un bucle infinito.

* `break`: Permite salir del bucle antes de que la condición deje de cumplirse.
* `continue`: Salta la iteración actual y continúa con la siguiente iteración.
* `else`: Se ejecuta cuando el bucle termina normalmente, es decir, sin que se haya usado `break`. De haber usado `break`, el bloque `else` no se ejecutará.

### Try Except
Bloque de código para manejar excepciones y errores. <br>
Ejemplo:
```python
numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")
```
## For
Bloque de codigo repetitivo para cada elemento en una secuencia. <br>
Ejemplo:
```python
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
   print(fruta) # Imprime cada fruta de la lista

cadena = "midudev"
for caracter in cadena:
   print(caracter) # Imprime cada caracter de la cadena
```
Esto se puede hacer con listas, cadenas y cualquier objeto iterable en Python.
>[!NOTE]
>Son más recomendados que while cuando conocemos cuántas veces queremos iterar.

### índice con For
Para obtener el índice de cada elemento en un bucle for, se puede usar la función `enumerate()`. <br>
Ejemplo:
```python
frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
   print(f"El índice es {index} y la fruta es {fruta}") # Imprime el índice y la fruta correspondiente
```
Puedes poner cualquier nombre a las variables que reciban el índice (primera posición) y el valor (segunda posición) dentro del bucle for.

### For anidados
Los bucles for pueden anidarse dentro de otros bucles for para iterar sobre múltiples secuencias. <br>
Ejemplo:
```python
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
   for numero in numeros:
       print(f"{letra}{numero}") # Imprime la combinación de cada letra con cada número
```
![](03_loops\Images\Python-Tutor-Example.png)

>![NOTE]
>Para ver cómo se ejecuta el código paso a paso, se puede probar en Python Tutor, una herramienta interactiva para analizar la ejecución de código en Python.

[Python Tutor](https://pythontutor.com/index.html)
![](03_loops\Images\Python-Tutor.png)

### Break y Continue
* `break`: Permite salir del bucle antes de que la condición deje de cumplirse.
* `continue`: Salta la iteración actual y continúa con la siguiente iteración.

### Comprensión de listas (list comprehension)
Es una forma concisa de crear listas a partir de otras listas o secuencias. <br>
Ejemplo:
```python
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus) # Imprime la lista de animales en mayúsculas
```
#### Condición dentro de list comprehension
También se pueden aplicar condiciones dentro de las comprensiones de listas para filtrar elementos. <br>
Ejemplo:
```python
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares) # [2, 4, 6]
```

### Rango (range)
La función `range()` se utiliza para generar una secuencia de números. Es comúnmente usada en bucles for. 
Por defecto, `range()` comienza en 0 y aumenta de 1 en 1.
Se puede especificar un inicio, un fin y un paso opcional. <br>
Por ejemplo: `range(2, 10, 2)`, `range(inicio, fin, paso)` <br>
Ejemplo:
```python
for num in range(0, 1000, 5):
   print(num) # Imprime los números del 0 al 1000 de 5 en 5

for num in range(10, 0, -1):
   print(num) # Imprime los números del 10 al 1 en orden descendente
```
>![WARNING]
>Range no crea una lista por sí misma, sino un objeto iterable que genera los números bajo demanda. 
>
>Para obtener una lista, se puede usar `list(range(...))`.
>
>Ejemplo:
>```python
>lista_numeros = list(range(10))
>print(lista_numeros) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>```

