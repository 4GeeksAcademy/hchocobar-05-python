"""
Condicionales:
 - Estructura if-elif-else
 - Operadores de comparación
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

""" for letter in message:
    print(letter, end='_')
print() """

for number in range(10, 40):
    if number % 5 == 0:
        continue
    print(number)
print('fin')
