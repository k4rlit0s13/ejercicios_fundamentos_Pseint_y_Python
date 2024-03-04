# # Hora futura

# # Escriba un programa que pregunte al usuario la 
# hora actual t del reloj y un número entero de horas h, que 
# indique qué hora marcará el reloj dentro de h horas:

horaActual=int(input("Ingresa la hora actual: "))
horaAvance=int(input("numero de horas que desea avanzar: "))
horaResultado=(horaActual+horaAvance)%24 #hora actual + la hora que se desea avanzar, se divide entre 24 horas para obtener la resta de estas para obtener la hora resultante
print("Despues de ", horaAvance,"horas, el reloj marcará las ", horaResultado, " horas")
