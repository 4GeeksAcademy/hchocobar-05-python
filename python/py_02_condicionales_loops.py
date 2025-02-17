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


number = 7
year = 2025

condition = number < 5 or year == 2025

def my_funtion():
    if number > 10 and year == 2025:
        result = number * 2
        print('mayor que 10', result)
        return True
    if condition:
        result = number * 5
        print('menor que 5', result)
        return False
    result = number + 10
    print('entre 5 y 10', result)
    return None

"""
for leter in message:
  print(leter)
# print('siempre se imprime')
"""

"""
for number in range(11):
    print(number)
"""

years = [2022, 2021, 2023, 2024, 2025, 2026, 2027]

for year in years:
    if year == 2021:
        continue
    if year == 2026:
        break
    print(year)


if 