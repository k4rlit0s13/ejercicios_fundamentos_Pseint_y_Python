

"""

Escriba un programa que determine si un 
caracter ingresado es letra, número, o ninguno
de los dos. En caso que sea letra, determine si 
es mayúscula o minúscula.

"""

letra=input("Ingrese un caracter: ")

if letra.isalpha(): # extension que nos deja saber si es una letra 
  print(f"El caracter '{letra}' es una {'mayúscula' if letra.isupper() else 'minúscula'}.") # el isupper nos ayuda a saber si es mayuscula
elif letra.isdigit(): # esta nos deja saber si es un digito
  print(f"El caracter '{letra}' es un número.")
else:
  print(f"El caracter '{letra}' no es una letra ni un número.")
