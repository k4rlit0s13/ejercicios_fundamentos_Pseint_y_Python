"""

Desarrolle un programa que solucione el problema de Solarrabietas:

"""

jugadorA=int(input("ingresa los puntos del jugador A: "))
jugadorB=int(input("ingresa los puntos del jugador B: "))
win1set=6


# para GANAR
if jugadorA>=6 and jugadorA-jugadorB==2: # aqui aplicamos si el jugador a es mayor que b diferente a 2 puntos, es el vencedor
    print("Gana A  ")
elif jugadorB>=6 and jugadorB-jugadorA==2:
    print("Gana B  ")
#PARA DESEMPATAR
elif jugadorA==5 and jugadorB==5:
    print("el ganador es el primero que llegue a 7")
elif jugadorA==6 and jugadorB==6:
    print("el set se define en un último juego")
#para continuar
elif jugadorA<=6 and jugadorB<=6 and jugadorA-jugadorB==1:
    print("el juego continua")
elif jugadorB<=6 and jugadorA<=6 and jugadorB-jugadorA==1:
    print("el juego continua")

else:
    print("error")
