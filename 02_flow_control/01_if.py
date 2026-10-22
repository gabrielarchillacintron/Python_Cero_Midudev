age = int(input("Introduce tu edad:\n"))
if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

nota = int(input("Introduce tu not del 0 al 10:\n"))
if nota <= 5:
    print("F")
elif nota == 6:
    print("D")
elif nota == 7:
    print("C")
elif nota == 8:
    print("B")
elif nota == 9:
    print("A")
else:
    print("No calificado")

edad = 20
tiene_dinero = True
 
if edad >= 18:
   if tiene_dinero:
      print("Puedes ir a la discoteca")
   else:
      print("Quédate en casa")
else:
   print("No puedes entrar a la disco")