n1=int(input("ingrese un numero: "))
n2=int(input("ingrese un numero: "))

n3=int(input("ingrese un numero: "))
n4=int(input("ingrese un numero: "))
n5=int(input("ingrese un numero: "))

n6=int(input("ingrese un numero: "))
n7=int(input("ingrese un numero: "))
n8=int(input("ingrese un numero: "))
n9=int(input("ingrese un numero: "))

def programa1():
    if n1<n2:
        return n1,n2
    elif n2>n1:
        return n2,n1
    else:
        return print("son iguales")
    

def programa2():
    ordenarNumeros3=sorted([n3,n4,n5])
    print(ordenarNumeros3)


def programa3():
    ordenarNumeros4=sorted([n6,n7,n8,n9])
    print(ordenarNumeros4)


print(programa1())
print(programa2())
print(programa3())