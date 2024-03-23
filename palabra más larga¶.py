

"""

Escriba un programa que pida al 
usuario dos palabras, y que indique 
cuál de ellas es la más larga y por 
cuántas letras lo es.

"""

print("ingresa 2 palabras por favor : ")

p1=input((" "))
p2=input((" "))

"""
tenemos que meter ahora la forma de que cuente los caracteres que hay en cada palabra para esto usamos len y para encontrar la diferencia usamos una resta
"""

diferencia1=len(p1)-len(p2) # aqui miramos si la diferencia es menor o mayor de la primera palabra frente a la segunda
diferencia2=len(p2)-len(p1) # aqui miramos si la diferencia es menor o mayor de la segunda palabra frente a la primera

if len(p1)>len(p2): # condición para mirar si primero la p1 es mayor que la p2 y por cuanto
    print("la palabra '",p1,"' es más larga que la palabra '",p2,"'"," esto por ", diferencia1," letras")
elif len(p1)<len(p2): # o si la p2 es mayor que la p1 y por cuanto
    print("la palabra '",p2,"' es más larga que la palabra '",p1,"'"," esto por ", diferencia2," letras")
else:                # o también si es que son iguales ambas palabras 
    print("la palabra '",p1,"' es igual a la palabra '",p2,"'"," esto por ", len(p1)," letras")


