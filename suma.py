#Círculos

#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

import math

radio=float(input("ingresa el radio del círculo que deseas sacarle el perímetro y el area: "))
perimetro= 2*math.pi*radio
area= math.pi*(radio**2)
print("El perímetro de tu círculo es de ",perimetro, "y el area es de ", area)

