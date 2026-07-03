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

age = 35
if age > 40:
    print('mayor de 40')
elif age > 20:
    print('menor de 40 y mayor de 20')
else:
    print('menor de 20')

#
while age > 30:
    age = age -1
    print(age)

print('se terminó el while')



""" 
lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
for item in lista:
    print(item)
"""

# range(inicio, fin no incluido, salto)  -> rango
for number in range(1, 100):
    if number % 20 == 0:
        continue
    if number % 5 == 0:
        text = f'{number} es el número elegido'
        print(text)

print('termino el for')