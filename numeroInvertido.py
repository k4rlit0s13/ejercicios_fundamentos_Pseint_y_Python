# Número invertido

# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

numero=input("usuario ingresa un número de 3 dígitos por favor: ")

if len(numero)==3 and numero.isdigit(): # len contará los caracteres de numero y numero debe ser digito
    numeroInverso=numero[::-1]
    print("El número invertido / al revez es: ",numeroInverso)
else:
    print("Usuario el número no es de 3 dígitos")