# Operadores de comparación
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 3)   # True
print(5 >= 5)   # True
print(5 <= 3)   # False

# Comparación de cadenas
print("manzana" < "pera") # True
print("Hola" == "hola") # False

# Variables Numericas y Cadenas de Texto como Booleanas
numero = 5
if numero: # True
   print("El número no es cero")
 
numero = 0
if numero: # False
   print("Aquí no entrará nunca")

nombre = "Juan"
if nombre:
   print("El nombre no es vacío")
 
nombre = ""
if nombre:
    print("El nombre no es vacío")
