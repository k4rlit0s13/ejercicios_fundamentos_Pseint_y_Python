"""

vamos a crear un algoritmo que nos 
muestre si un dato ingresado por 
consola es par o impar

"""

# Primero dejamos ingrear una variable al usuario pero este debe ser un entero
Numero=int(input("Porfavor ingresa un número para saber si es par o no: "))


if Numero%2==0: # ahora pondré una condición que sea que si su reciduo al dividir por 2 es 0 es par


    
    print("El número ",Numero," es par") # si nuestra condición se cuemple le diremos al usuario que fectivamente es par



else:                                                   #sin embargo si no es así le diremos el contrario, que es impar
    print("Me temo que el número",Numero ," es impar")