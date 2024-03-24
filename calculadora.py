"""

Escriba un programa que simule una calculadora 
básica, este puede realizar operación de suma, 
resta, multiplicación y división.

El programa debe recibir como entrada 2 números 
reales y un operador, que puede ser +, -, * o /.

La salida del programa debe ser el resultado de 
la operación.


"""

n1=int(input("Ingresa un valor"))
n2=int(input("Ingresa otro valor"))
operador=input("Ingresa un operador +,-,*,/ : ")

if operador=="+":
    suma=n1+n2
    print(suma)

elif operador=="-":
    resta=n1-n2
    print(resta)

elif operador=="*":
    multiplicacion=n1*n2
    print(multiplicacion)

elif operador=="/":
    division=n1/n2
    print(division)

