###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("Ejercicio 1: Determinar el mayor de dos números")
print("Introduzca dos números")
primer_numero = int(input("Primer número:"))
segundo_numero = int(input("Segundo número:"))
if primer_numero == segundo_numero:
    print("Los numeros son iguales")
elif primer_numero > segundo_numero:
    print(f"El numero mayor es: {primer_numero}.") 
else:
    print(f"El numero mayor es: {segundo_numero}.")        

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("Ejercicio 2: Calculadora simple")
print("Introduzca dos números y una operacion (+, -, *, /)")
num1 = float(input("Primer número:"))
num2 = float(input("Segundo número:"))
operacion = input("Operacion:")
if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        print(num1 / num2)
else:
    print("Operación no válida.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("Ejercicio 3: Año bisiesto")
año = int(input("Introduzca un año:"))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("Este es un año bisiesto.")
else:
    print("No es bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("Ejercicio 4: Categorizar edades")
edad = int(input("Introduzca edad:"))
if 0<= edad <= 2:
    print("Bebe")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("No valida.")