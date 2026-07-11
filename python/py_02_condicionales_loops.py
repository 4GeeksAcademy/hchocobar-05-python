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
# name = 'Hector'  # Variable string
# message = 'Bienvenido!' # Variable string
# print('Hola', name, message)

"""
age = 25
if age >= 18:
    print('el doble de la edad es', age * 2, end='---')
    print('mayor de edad')
elif age >= 16:
    print('noes mayor de edad tiene mas de 16')
else:
    print('MENOR DE 16')

print('fuera del condicional') """

# PEP8, antes y despues de todo operador, escribir un espacio en blanco
cadena = 'Hola Mundo'
"""
for letra in cadena:
    if letra != ' ':
        print(letra, end=' ')
    else:
        print()
print()
"""

# range(inicio=0, fin-1, salto=1)
for number in range(2, 20, 2):
    print(number, end=' - ')
print()

