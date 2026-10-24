###
# EJERCICIOS (for)
###
print("EJERCICIOS (for)")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

print("\nEjercicio 1:")
for numero in range(21):
    if numero % 2 == 0:
        print(numero)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
    suma += numero
media = suma / len(numeros)
print(media)


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(maximo)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
lista = []
for palabra in palabras:
    if len(palabra) > 5:
        lista.append(palabra)
print(lista)

lista = []
lista = [palabra for palabra in palabras if len(palabra) > 5]
print(lista)



# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
count = 0
print(palabras)
letra = []
# letra = input("Introduzca una letra: ")
seguir = True
while seguir:
    letra = input("Introduzca una letra: ")
    if letra == "Salir" or letra == "salir":
        seguir = False
    for palabra in palabras:
        for _ in palabra[0]:
            if letra == _:
                count += 1
            continue
    print(count)
    count = 0


###
# EJERCICIOS (range)
###

print("\nEJERCICIOS (range)")

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().

print("\nEjercicio 1:")
for numero in range(1,11):
    print(numero)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

print("\nEjercicio 2:")
for numero in range(21):
    if not numero % 2 == 0:
        print(numero)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

print("\nEjercicio 3:")
for numero in range(5,51):
    if numero % 5 == 0:
        print(numero)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

print("\nEjercicio 4:")
for numero in range(10, 0, -1):
    print(numero)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

print("\nEjercicio 5:")
suma = 0
for numero in range(1, 101):
    suma += numero
print(suma)
    

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

print("\nEjercicio 6:")
seguir = True
while seguir:
    numero = input("Introdusca un numero: ")
    if numero == "Salir" or numero == "salir":
        seguir = False
    try:
        for _ in range(1, 11):
            print(int(numero)*_)
    except:
        print("No es un numero.")