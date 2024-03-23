#Años bisiestos

"""

un programa que indique si un año es 
bisiesto o no, teniendo en cuenta cuál 
era el calendario vigente en ese año

"""

# le pediremos al usuario que introdusca un valor

Año=int(input("Por favor ingresa un año: "))



if Año<=1582: # todo se define desde 1582 antes o despues, es un punto central, condicionamos este punto si es menor o igual                                                                                                        
    Resultado=Año%4==0 #aqui se agrega una condición por el calendario juliano
    print("El año ",Año , " es bisiesto en el calendario juliano(antes de 1582)") # si se cumple es bisiesto

elif(Año%4==0 and not Año%100==0) or Año%400==0: # miraremos ahora el calendario gregoriano, si es divisible entre cuatro y no en 100 o divisble en 400
    print("El año ",Año ," es bisiesto en el calendario gregoriano(despues de 1582)")

else:
    print("El año ",Año," no es bisiesto") # si no solo desimos que no lo es y listo