# Casting de tipos para convertir un tipo de dato a otro.
print(type(int("10"))) # <class 'int'>

# De esta forma podemos interactuar con diferentes tipos de datos y realizar operaciones entre ellos.
print(int("10") + 5) # 15
print(int(3.14)) # 3

# Numeros a booleanos, 0 es False y cualquier otro número es True.
print(bool(0)) # False
print(bool(1)) # True
print(bool(-1)) # True

# Cadenas a booleanos, una cadena vacía es False y cualquier otra cadena es True.
print(bool("")) # False
print(bool("Hola")) # True

# Redondeo
print(round(3.14)) # 3
print(round(3.5)) # 4
print(round(2.5)) # 2