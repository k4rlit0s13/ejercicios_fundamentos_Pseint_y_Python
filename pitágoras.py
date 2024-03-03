# Pitágoras

# Escriba un programa que reciba como entrada las longitudes de los dos catetos a
# y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

catetoA=float(input("ingrese el cateto A: "))
catetoB=float(input("ingrese el cateto B: "))
hipotenusa=(catetoA**2+catetoB**2)**0.5
print(hipotenusa)