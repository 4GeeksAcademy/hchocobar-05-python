"""
Format String
https://docs.python.org/es/3/tutorial/inputoutput.html#fancier-output-formatting

método: str.format()
Documentación: https://docs.python.org/es/3/library/string.html#format-string-syntax

Literales de cadena formateados (también llamados f-strings)
Documentación: https://docs.python.org/es/3/tutorial/inputoutput.html#formatted-string-literals

"""

# Opción 1
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

text = 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
print(text)
