"""
Colecciones
- Listas,       list: coleccion ordenada y mutable de elementos separados por comas entre corchetes []
- Tuplas,      tuple: colección ordenadas e inmutable de elementos separados por comas entre paréntesis ()
- Conjuntos,     set: colección no ordenada y de elementos distintos separados por comas entre llaves {}
- Diccionarios, dict: colección indexada de elementos pares 'clave': valor y mutables separados por comas entre llaves {}

Funciones comunes de las colecciones
  - list(), tuple(), set(), dict()
  - len()
  - type()

Métodos comunes de las colecciones
  - .insert()
  - .append()
  - .sort()
  - .reverse()
  - Métodos de string: https://docs.python.org/3/library/stdtypes.html#string-methods
  - Métodos de listas: https://docs.python.org/es/3/tutorial/datastructures.html#more-on-lists 
  - Métodos de diccionarios: https://docs.python.org/3/library/stdtypes.html?highlight=dict%20method#mapping-types-dict

Tips diccionarios
  - método .get()  # deveulve el valor de la clave del argumento o None si no existe.
  - método .items()  # devuelve el par 'clave': valor y nos permite desempaquetar
  - operador in  # para verificar si una clave existe en un diccionario
"""
def my_error():
  print('tengo un error')


message = 'Bienvenido hola mundo '

students = ['Agustin', 'Alejandro', 'Anais', 'Bilbo', 'David', 'Gabriela', 'Fidel', 
            'Mar', 'Marco', 'Matias', 'Mery', 'Pablo', 'Pau', 'Robert', 'Victoria', 'Eduardo']

months = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'dicienbre')

person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]

category = {'python', 'react', 'html', 'python', 'html', 'css'}

"""
data = category
print(data)
print(type(data), len(data))
"""

"""
if 'name' in person:
    print(person['name'])
else:
    print('no tiene la clave "name"')
"""

row = person.get('email', None)
if not row:
    my_error()
else:
    print(row)
