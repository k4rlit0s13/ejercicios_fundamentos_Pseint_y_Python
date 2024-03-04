# Parte decimal

# Escriba un programa que entregue la parte decimal 
#de un número real ingresado por el usuario.

real=float(input("Ingrese el número decimal: "))
entero=int(real)
decimal=real-entero
print("La parte decimal de ",real, "es",decimal)