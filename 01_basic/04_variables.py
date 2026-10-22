# Tipado dinamico
str_variable = "Hola"
print(type(str_variable)) # <class 'str'>
str_variable = 10
print(type(str_variable)) # <class 'int'>

# Tipado fuerte
print(10 + "5") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10 + int("5")) # 15

# Cadenas literales formateadas (f-strings)
name = "Alice"
age = 30
print(f"Me llamo {name} y tengo {age} años.") # Me llamo Alice y tengo 30 años.

# Tipado estatico
variable = "nombre"
variable = 42
variable = str = "palabra"


