"""
- Format String: https://docs.python.org/es/3/tutorial/inputoutput.html#fancier-output-formatting
  1. Método: str.format(): https://docs.python.org/es/3/library/string.html#format-string-syntax
  2. Literales de cadena formateados: f-strings: https://docs.python.org/es/3/tutorial/inputoutput.html#formatted-string-literals.
  3. Viejo formateo de cadenas: %: https://docs.python.org/es/3/tutorial/inputoutput.html#old-string-formatting
"""
pi = 3.14
animals = 'eels'

# Ejemplo 1
print('{2}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))  # 3.1+ only

# Ejemplo de f-string
print(f'The value of pi is approximately {pi:.3f}.')
print(f'My hovercraft is full of {animals}.')

# Ejemplo del 3
print('The value of pi is approximately %5.3f.' % pi)
