
"""

Escriba un programa que pida dos 
números enteros y que calcule la 
división, indicando si la división 
es exacta o no.

"""

# dejaremos que meta una división nuestro usuaio
print("Porfavor usuario introduce 2 números dividiendo y divisor respectivamente: ")
dividendo=int(input(" "))
divisor=int(input(" "))

dividiendado=dividendo%divisor

if dividiendado==0:
    print("La división es exacta, ",dividiendado," es el resultado")
else:
    print("La división no es exacta, ",dividiendado," es el resultado")