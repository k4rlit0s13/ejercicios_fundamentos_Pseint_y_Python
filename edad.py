"""
Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
"""

 #importar funciones de tiempo


import datetime

# Introduce la fecha de nacimiento en formato 'YYYY-MM-DD'
fechaNacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

# Calcula la edad a partir de la fecha de nacimiento
fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, '%Y-%m-%d')
edad = datetime.datetime.now().year - fechaNacimiento.year
# Imprime la edad calculada

print("Tu edad es:", edad)