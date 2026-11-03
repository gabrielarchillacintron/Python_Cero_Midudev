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

def imprimir_pares(inicio=0, final=0):
    while True:
        inicio = int(input("Introduce el número de inicio (o -1 para salir): "))
        if inicio == -1:
            break
        final = int(input("Introduce el número final: "))
        for numero in range(inicio, final + 1):
            if numero % 2 == 0:
                print(numero)
    else:
        print("Fin de la impresión de números pares.")
        return None
    
imprimir_pares()

print("___________________")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

print("Ejercicio 2: Calcular la media de una lista")

def calcular_media():
    numeros = []
    while True:
        entrada = input("Introduce uno o varios números (o escribe 'salir' para terminar): ").strip()
        if entrada.lower() == "salir":
            break
        if entrada == "":
            numeros = []
            print("No se ingresaron números.")
            continue
        try:
            nuevos_numeros = [int(numero) for numero in entrada.split()]
        except ValueError:
            print("Introduce únicamente números enteros.")
            continue

        numeros.extend(nuevos_numeros)
        media = sum(numeros) / len(numeros)
        print(f"La media de la lista {numeros}: {media}")
        numeros = []

    print("No se ingresaron números.")
    print("Fin del cálculo de la media.")
    return None

calcular_media()


print("___________________")


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

print("Ejercicio 3: Buscar el máximo de una lista")

def maximo_lista():
    while True:
        entrada = input("Introduce números separados por espacios (o escribe 'salir' para terminar): ").strip()
        if entrada.lower() == "salir":
            break
        try:
            numeros = [int(numero) for numero in entrada.split()]
        except ValueError:
            print("Introduce únicamente números enteros.")
            continue

        if not numeros:
            print("No se ingresaron números.")
            continue

        maximo = numeros[0]
        for numero in numeros:
            if numero > maximo:
                maximo = numero
        print(f"El número máximo es: {maximo}")

    print("Fin de las pruebas.")

maximo_lista() 

print("___________________")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

print("Ejercicio 4: Filtrar cadenas por longitud")

def filtrar_por_longitud5():
    while True:
        palabras = input("Introduce una lista de palabras separadas por espacio (o escribe 'salir' para terminar): ")
        lista_filtrada = []
        if palabras.strip().lower() == "salir":
            break

        lista = palabras.split()

        for palabra in lista:
            if len(palabra) > 5:
                lista_filtrada.append(palabra)
        
        print(f"Las palabras con más de 5 letras en la lista {lista}:", {lista_filtrada})
    print("Fin de las pruebas.")

filtrar_por_longitud5()


print("___________________")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("Ejercicio 5: Contar palabras que empiezan con una letra")

def palabras_que_empiezan_con():
    while True:
        count = 0
        palabras = input("Introduce una lista de palabras separadas por espacio (o escribe 'salir' para terminar): ")
        if palabras.strip().lower() == "salir":
            break
        letra = input("Introduce una letra: ").lower()
        lista = palabras.split()

        for palabra in lista:
            if palabra.lower().startswith(letra):
                count += 1

        if count == 0:
            print("No se encuentra ninguna.")
            continue

        print(f"En la lista de palabras {lista}, {count} palabras empiezan con la {letra}.")
    print("Fin de las pruebas.")

palabras_que_empiezan_con()

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
    while True:
        inicial = input("Introduce un número inicial (o escribe 'salir' para terminar): ")

        if inicial.lower() == "salir":
            break

        final = input("Introduce un número final: ")

        try:
            for numero in range(int(inicial), int(final) + 1):
                    print(numero)
        except:
            print("Numeros entrados no validos.")
    print("Fin de las pruebas.")

numeros_del_1_al_10()

print("___________________")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

print("Ejercicio 2: Imprimir números impares del 1 al 20")

def numeros_impares_del_1_al_20():
    while True:
        inicial = input("Introduce un número inicial (o escribe 'salir' para terminar): ")

        if inicial.lower() == "salir":
            break

        final = input("Introduce un número final: ")

        try:
            for numero in range(int(inicial), int(final) + 1):
                if numero % 2 != 0:
                    print(numero)
        except:
            print("Numeros entrados no validos.")
    print("Fin de las pruebas.")

numeros_impares_del_1_al_20()

print("___________________")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

print("Ejercicio 3: Imprimir múltiplos de 5")

def multiplos_de_5():
    while True:
        numero = input("Introduce un número (o escribe 'salir' para terminar): ")

        if numero.lower() == "salir":
            break        

        final = input("Introduce multiplo final: ")

        try:
            for i in range(int(numero), int(final) + 1):
                if i % int(numero) == 0:
                    print(i)
        except:
            print("Numeros entrados no validos.")
    print("Fin de las pruebas.")

multiplos_de_5()

print("___________________")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

print("Ejercicio 4: Imprimir números en orden inverso")

def  numeros_orden_inverso():
    while True:
        inicial = input("Introduce un número inicial (o escribe 'salir' para terminar): ")

        if inicial.lower() == "salir":
            break        

        final = input("Introduce un numero final: ")

        try:
            for i in range(int(final), int(inicial) - 1, -1):
                print(i)
        except:
            print("Numeros entrados no validos.")
    print("Fin de las pruebas.")

numeros_orden_inverso()

print("___________________")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

print("Ejercicio 5: Suma de números en un rango")

def suma_numeros_del_1_al_100():
    while True:
        suma = 0
        inicial = input("Introduce un número inicial (o escribe 'salir' para terminar): ")

        if inicial.lower() == "salir":
            break        

        final = input("Introduce un numero final: ")

        try:
            for i in range(int(inicial), int(final) + 1):
                suma += i
            print(suma)
        except:
            print("Numeros entrados no validos.")
    print("Fin de las pruebas.")

suma_numeros_del_1_al_100()

print("___________________")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

print("Ejercicio 6: Tabla de multiplicar")

def tabla_multiplicar():
    while True:
        numero = input("Introduce un número: ")
        if numero.lower() == "salir":
            break 
        inicial = input("Introduce un número inicial (o escribe 'salir' para terminar): ")
        final = input("Introduce un numero final: ")
        try:
            for i in range(int(inicial), int(final) + 1):
                print(f"{int(numero)} x {i} = {int(numero) * i}")
        except:
            print("Numeros entrados no validos.")
    print("Fin de las pruebas.")

tabla_multiplicar()

print("___________________")

print("|||||||||||||||||||")