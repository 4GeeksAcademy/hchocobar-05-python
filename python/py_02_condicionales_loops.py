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

""" 
edad = 10
if edad < 20:
    print('la edad es menor a 20')
    edad += 2
else:
    print('mayor de 30')
"""
numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]
cadena = 'Condicionales'

for number in numbers:
    if number % 2 == 0:
      # print(number)
      pass

for letra in cadena:
    # print(letra)
    pass

# range(start, stop - 1, step)
for number in range(len(numbers)):
    print(number)