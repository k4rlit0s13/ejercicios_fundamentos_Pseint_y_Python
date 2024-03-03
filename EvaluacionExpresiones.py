"""Evaluación de expresiones"""

# Sin usar el computador, evalúe las siguientes expresiones, y para cada una de ellas indique el resultado y su tipo (si la expresión es válida) o qué error ocurre (si no lo es):

# 2+3 es tipo int, dando 5
# 4/0 da error, division entre 0
# 5+3*2 da 11 es int
# 2 ** 10 == 1000 or 2 ** 7 == 100 booleano y exponente, son incorrectos error, falsos
# int("cuarenta") es error porque nesecita un valor numérico y tiene un valor de texto
# 70/16 + 100/24 es tipo float ya que es un decimal el resultado, no un numero entero
# 200 + 19% error, % es la resta de la división de 2 digitos aqui solo hay 1, no se pueden sumar amenos que sea 0.19 que si sería porcentaje
# 3 < (1024 % 10) < 6 es boolean, siendo true, resultado de la resta de la división 1
# 'six' + 'eight' concatenación, resultado es sixeight
# 'six' * 'eight'error, no se pueden multiplicar cadenas de texto
# float(-int('5') + int('10')) es error ya que se ponen numeros enteros como cadenas de texto y estas no se pueden operar
# abs(len('ocho') - len('cinco')  resultado: 1 len cuenta cuandos caracteres hay osea 4 y 5 los resta y abs saca el valor absoluto sin signos
# bool(14) or bool(-20) bool vuelve los valores booleanos por lo que bool() pone como factor que el valor dentro si es distinto a 0 es true, asi que la respuesta es: true, ambos son distintos a 0
# float(str(int('5' * 4) / 3)[2]) respuesta:5.0 ya que "5"*4="5555"se pasa a entero 5555/3=1851.66666,str lo vuelve cadena de texto"1851.6666",[2]accede a la posición de caracteres 2= numero5 y float lo vuelve decimal=5.0