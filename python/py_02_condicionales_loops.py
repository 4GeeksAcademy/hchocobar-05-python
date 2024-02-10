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
name = 'Hector'  # Variable string
message = 'Bienvenido!' # Variable string
# print('--- Hola', name, message)

number = 5
is_admin = True

# iterables
""" for letter in message:
    print(letter) """

for foo in range(0, 20, 1):
    if foo % 3 == 0:
        continue    
    print(foo)
