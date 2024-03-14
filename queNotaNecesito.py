certamen1=float(input("ingrese el certamen 1 la nota: "))
certamen2=float(input("ingrese el certamen 1 la nota: "))
laboratorio=float(input("ingrese la nota del laboratorio: "))

promedioCertamen=(certamen1+certamen2+laboratorio)/3

notaFaltante=(60-(promedioCertamen*0.7))/3

print("La nota necesaria es la siguiente: ",notaFaltante)

