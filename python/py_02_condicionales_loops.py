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
""" 
number = 10
if number > 18:
    print('mayor de edad')
elif number > 12:
    print('es adolescente')
elif number > 1:
    print('es un niño')
else:
    print('es un bebe')

for letter in message:
    print(letter)
"""


for foo in range(10):
    if foo % 2 == 0:
        continue
    if foo == 3:
        pass
    if foo == 5:
        break
    print(foo)

