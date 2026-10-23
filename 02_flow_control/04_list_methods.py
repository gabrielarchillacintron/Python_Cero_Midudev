###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
lista1.append('e') # Añade un elemento al final
print(lista1) # ['a', 'b', 'c', 'd', 'e']

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1) # ['a', '@', 'b', 'c', 'd', 'e']

lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(lista1) # ['a', '@', 'b', 'c', 'd', 'e', '😃', '😍']

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1) # ['a', 'b', 'c', 'd', 'e', '😃', '😍']

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(ultimo) # '😍'
print(lista1) # ['a', 'b', 'c', 'd', 'e', '😃']

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1) # ['a', 'c', 'd', 'e', '😃']

# Eliminar por lo bestia un índice
del lista1[-1]
print(lista1) # ['a', 'c', 'd', 'e']

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1) # []

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1) # ['🐼', '😿', '🐹']

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers) # [2, 3, 8, 10, 99, 101]

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # [2, 3, 8, 10, 99, 101]

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas) # ['limón', 'limón', 'manzana', 'manzana', 'pera', 'pera']

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas) # ['manzana', 'manzana', 'pera', 'pera', 'limón', 'limón']

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

# Buscar el índice de un elemento
print(animals.index('🐼')) # Devuelve el índice de la primera aparición -> 1

# Si el elemento no existe, index() lanza un error (ValueError)
# Por eso conviene comprobar antes con "in", o usar try/except
# if '🦁' in animals:
#    print(animals.index('🦁'))
# else:
#    print('🦁 no está en la lista')

# index() también acepta un rango de búsqueda (inicio, fin)
animals = ['🐶', '🐼', '🐨', '🐶']
print(animals.index('🐶', 1)) # Busca '🐶' a partir del índice 1 -> 3