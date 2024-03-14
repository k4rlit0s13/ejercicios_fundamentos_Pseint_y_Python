

import math

hPequeño=47
hGrande=67
gxcm=1.038
ccalórica=3.7
conductividadTermica=5.4e-3
tAguaEbullicion=100

tOriginal=float(input("ingresa la temperatura original del huevo en °C  : "))
tDeseada=float(input("ingresa la temperatura deseada del huevo en c°(posible hasta 70°C): "))

promedioMasaHuevo=(hPequeño+hGrande)/2

tiempo=(promedioMasaHuevo**(2/3))*(ccalórica**(1/3))*(gxcm**(1/3))/(conductividadTermica*math.pi**2)*(4*math.pi/3)**(2/3)*math.log(0.76*(tOriginal-tDeseada)/(tDeseada-tAguaEbullicion))
if tiempo < 0:
    tiempo = abs(tiempo)  # Tomar el valor absoluto si es negativo
    
print("El tiempo necesario para llegar a ", tDeseada, " es de ",tiempo, " segundos")