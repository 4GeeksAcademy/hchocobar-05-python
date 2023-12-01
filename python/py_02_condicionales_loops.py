"""
Condicionales
 - Estructura if-elif-else
 - Operadores lógicos: and  or  not

Loops
 - while
 - for in 
  - iterables
  - range(start, stop, step)
 - break, continue

Identación y bloques
  - pass
"""

# Hola Mundo
is_login = True
is_admin = False

if is_login:
    pass
else:
    print("por favor, login")

students = ['Andres', 'Alejandro', 'Daniel', 'Evelyn', 'Emiko', 'Guido', 'Leire', 
           'Lorenzo', 'Lourdes', 'Majo', 'Merlina', 'Mike', 'Pau', 'Sara' ,'Yoel']


palabra = 'palabra larga'

# interables: cadenas, listas, tuplas, diccionarios, conjuntos
""" for item in palabra:
    print(item) """

for item in range(10):
    if item % 5 != 0:
        break
    print(item)
