"""
Condicionales:
 - Estructura if-elif-else
 - Operadores lógicos: and  or  not

Loops:
 - while
 - for in 
  - iterables
  - range(start, stop, step)
 - break, continue

Identación y bloques
  - pass
"""

# Hola Mundo
name = 'Hector'  # Variable string
message = 'Bienvenido!' # Variable string
# print('Hola', name, message)
condicion = True

""" if condicion:
    print(name)
else:
    pass
 """

""" for letter in message:
    print(letter)
"""

for item in range(1,11):  # 1, 3, 5, 7, 9
    if item % 2 == 0:
        print(item)
        continue
        print('no se imprime')
    print('hola')

# breack - salta / sale del ciclo inmediatamente
# continue - Vuelve al inicio del ciclo sin ejecutar las lineas posteriores