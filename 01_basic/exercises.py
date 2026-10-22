###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

print("--------------")

### Completa aquí
print("Respuesta:")
name = "Gabriel"
city = "Ponce, Puerto Rico"
print(name + "\n" + city)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print("--------------")

### Completa aquí
print("Respuesta:")
print(
    f"Tipo de dato de a: {type(a)}\n"
    f"Tipo de dato de b: {type(b)}\n"
    f"Tipo de dato de c: {type(c)}\n"
    f"Tipo de dato de d: {type(d)}\n"
    f"Tipo de dato de e: {type(e)}"
)

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

print("--------------")

### Completa aquí
print("Respuesta:")
cadena = "12345"
entero = int(cadena)
flotante = float(entero)

print(f"Entero: {entero}")
print(f"Flotante: {flotante}")

decimal = 3.99
entero_decimal = int(decimal)

print(f"Decimal: {decimal}")
print(f"Entero a partir del decimal: {entero_decimal}. ¿Qué ocurre? Se pierde la parte decimal al convertir a entero.")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

print("--------------")

### Completa aquí
print("Respuesta:")
name = "Gabriel"
age = 26
height = 5.10

print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} pies.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print("--------------")

print("Respuesta:")
respuesta = int(round(3.14159) // 2)
print("PI = 3.14159")
print("Pi redondeado = ", round(3.14159))
print("División entera entre el número PI redondeado y 2 = ", respuesta)