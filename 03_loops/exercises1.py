###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

print("--------------")
print("\nEjercicio 1:")
count = 10
while count != 0:
    print(count)
    count -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

print("--------------")
print("Ejercicio 2:")
count = 1
suma = 0
while count <= 20:
    if count % 2 == 0:
        suma += count
    count += 1
print(suma)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("--------------")
print("Ejercicio 3:")
numero = 1
factorial = 1
while True:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero <= 0:
            print("Debe ser positivo.")
            continue

        while numero > 0:
            factorial *= numero
            numero -= 1
        print(factorial)
        factorial = 1
        
    except:
        print("No es un numero.")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

print("--------------")
print("Ejercicio 4:")
pasword = ""
while len(pasword) < 8:
    pasword = input("Pasword: ")
    if len(pasword) < 8:
        print("8 caracteres minimo.")
print("Contraseña válida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

print("--------------")
print("Ejercicio 5:")
numero = 0
factor = 1
while True:
    try:
        numero = int(input("Escribe un número: "))
        while factor != 11:
            print(f"{numero} * {factor} = {numero*factor}")
            factor += 1
        print("Fin")
        factor = 1
        continue
        
    except:
        print("No es un numero.")


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("--------------")
print("Ejercicio 6:")
n = 0
numero = 2
while True:
    try:
        n = int(input("Escribe un número positivo N: "))
        if n <= 0:
            print("Debe ser positivo.")
            continue

        while numero <= n:
            es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
            divisor = 2
            while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
                if numero % divisor == 0:
                    es_primo = False  # Si encontramos un divisor, no es primo
                    break  # Salimos del bucle interior
                divisor += 1
            if es_primo:
                print(numero)
            numero += 1
        numero = 2
        continue

    except:
        print("No es un numero.")

print("--------------")