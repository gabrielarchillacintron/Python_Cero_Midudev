# Ejemplo Basico de Lista
lista = [1, 2, 3, 4, 5]
print(lista)

# Lista con distintos tipos de elementos
lista_mixta = [1, "Hola", 3.14, True]
print(lista_mixta)

# Identificar tipos de elementos en la lista
# lista = list(int | str | float | bool) = [1, "Hola", 3.14, True]

# Lista de listas (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)

# Acceder a elementos de una lista
lista = [10, 20, 30, 40, 50]
print(lista[0])  # 10
print(lista[2])  # 30
print(lista[-1]) # 50 (último elemento)

# Slicing de listas
print(lista[1:4])  # [20, 30, 40] (sublista desde el índice 1 hasta el 3)
print(lista[:3])   # [10, 20, 30] (sublista desde el inicio hasta el índice 2)
print(lista[2:])   # [30, 40, 50] (sublista desde el índice 2 hasta el final)
print(lista[:])    # [10, 20, 30, 40, 50] (toda la lista)
print(lista[::2])  # [10, 30, 50] (sublista con paso 2)
print(lista[::3])  # [10, 40] (sublista con paso 3)
print(lista[::-1]) # [50, 40, 30, 20, 10] (sublista en orden inverso)

# Modificar elementos de una lista
lista[1] = 25
print(lista)  # [10, 25, 30, 40, 50]

# Agregar elementos a una lista
lista = [10, 20, 30]
lista.append(40)  # Agrega un solo elemento al final de la lista
print(lista)  # [10, 20, 30, 40]
lista.extend([50, 60])  # Agrega múltiples elementos al final de la lista
print(lista)  # [10, 20, 30, 40, 50, 60]
lista = lista + [70, 80]  # Agrega múltiples elementos al final de la lista
print(lista)  # [10, 20, 30, 40, 50, 60, 70, 80]
lista += [90, 100]  # Agrega múltiples elementos al final de la lista
print(lista)  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

