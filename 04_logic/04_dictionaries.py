###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# para acceder a los valores
print(persona["nombre"]) # midudev
print(persona["calificaciones"][2]) # 9
print(persona["socials"]["twitter"]) # @midudev

# cambiar valores al acceder
persona["nombre"] = "madeval"
persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
del persona["edad"]
# print(persona)

# eliminar y obtener un valor al mismo tiempo
es_estudiante = persona.pop("es_estudiante") 
print(f"es_estudiante: {es_estudiante}") # True
print(persona) # {'nombre': 'madeval', 'calificaciones': [7, 8, 10], 'socials': {'twitter': '@midudev', 'instagram': '@midudev', 'facebook': 'midudev'}}

# sobreescribir un diccionario con otro diccionario
a = { "name": "miduev", "age": 25 } # diccionario original
b = { "name": "madeval", "es_estudiante": True } # diccionario a actualizar

a.update(b) # actualiza el diccionario a con los valores de b
print(a) # {'name': 'madeval', 'age': 25, 'es_estudiante': True}

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# obtener todas las claves
print("\nkeys:") # muestra todas las claves del diccionario
print(persona.keys()) # dict_keys(['nombre', 'calificaciones', 'socials'])

# obtener todas los valores
print("\nvalues:") # muestra todos los valores del diccionario
print(persona.values()) # dict_values(['madeval', [7, 8, 10], {'twitter': '@midudev', 'instagram': '@midudev', 'facebook': 'midudev'}])

# obtener tanto clave como valor
print("\nitems:") # muestra todos los pares clave-valor del diccionario
print(persona.items()) # dict_items([('nombre', 'madeval'), ('calificaciones', [7, 8, 10]), ('socials', {'twitter': '@midudev', 'instagram': '@midudev', 'facebook': 'midudev'})])

for key, value in persona.items():
  print(f"{key}: {value}") # imprime cada par clave-valor del diccionario