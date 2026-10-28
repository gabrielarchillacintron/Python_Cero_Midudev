# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

###
# EJERCICIOS (for)
###
print("|||||||||||||||||||")
print("Ejercicios (for)")
print("___________________")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

print("Ejercicio 1: Imprimir números pares")

def imprimir_pares(inicio, final):
    for numero in range(inicio, final + 1):
        if numero % 2 == 0:
            print(numero)
    
print("Los números pares del 2 al 20 son:")
imprimir_pares(inicio=2, final=20)

print("___________________")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

print("Ejercicio 2: Calcular la media de una lista")

def calcular_media(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros) if numeros else 0

numeros = [10, 20, 30, 40, 50]
print(f"La media de la lista {numeros}:", calcular_media(numeros))

print("___________________")


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

print("Ejercicio 3: Buscar el máximo de una lista")

def maximo_lista(numeros):
    maximo = numeros[0] if numeros else None
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo

numeros = [15, 5, 25, 10, 20]
print(f"El máximo de la lista {numeros}:", maximo_lista(numeros))

print("___________________")


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

print("Ejercicio 4: Filtrar cadenas por longitud")

def filtrar_por_longitud5(palabras):
    lista_filtrada = [palabra for palabra in palabras if len(palabra) > 5]
    return lista_filtrada

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
print(f"Las palabras con más de 5 letras en la lista {palabras}:", filtrar_por_longitud5(palabras))

print("___________________")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("Ejercicio 5: Contar palabras que empiezan con una letra")

def palabras_que_empiezan_con(palabras, letra):
    count = 0
    letra = letra.lower()
    if letra == "Salir" or letra == "salir":
        print("Saliendo...")
        return None
    for palabra in palabras:
        if palabra.lower().startswith(letra):
            count += 1
    return count

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
print(f"Lista de palabras: {palabras}")
letra = input("Introduce una letra (o 'salir' para terminar): ")
resultado = palabras_que_empiezan_con(palabras, letra)

while resultado is not None:
    print(f"Hay {resultado} palabras que empiezan con la letra '{letra}' en la lista {palabras}")
    letra = input("Introduce una letra (o 'salir' para terminar): ")
    resultado = palabras_que_empiezan_con(palabras, letra)

###
# EJERCICIOS (range)
###

print("|||||||||||||||||||")
print("Ejercicios (range)")

print("___________________")

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().

print("Ejercicio 1: Imprimir números del 1 al 10")

def numeros_del_1_al_10():
    for numero in range(1, 11):
        print(numero)

numeros_del_1_al_10()

print("___________________")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

print("Ejercicio 2: Imprimir números impares del 1 al 20")

def numeros_impares_del_1_al_20():
    for numero in range(1, 21):
        if numero % 2 != 0:
            print(numero)

numeros_impares_del_1_al_20()

print("___________________")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

print("Ejercicio 3: Imprimir múltiplos de 5")

def multiplos_de_5():
    for numero in range(5, 51):
        if numero % 5 == 0:
            print(numero)

multiplos_de_5()

print("___________________")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

print("Ejercicio 4: Imprimir números en orden inverso")

def  numeros_orden_inverso():
    for numero in range(10, 0, -1):
        print(numero)

numeros_orden_inverso()

print("___________________")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

print("Ejercicio 5: Suma de números en un rango")

def suma_numeros_del_1_al_100():
    suma = 0
    for numero in range(1, 101):
        suma += numero
    return suma

print(f"La suma de los números del 1 al 100 es: {suma_numeros_del_1_al_100()}")

print("___________________")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

print("Ejercicio 6: Tabla de multiplicar")

def tabla_multiplicar():
    numero = int(input("Introduce un número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar()

print("___________________")

print("|||||||||||||||||||")