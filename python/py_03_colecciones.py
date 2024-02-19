"""
Colecciones
- Listas, list: coleccion ordenada y mutable de elementos separados por comas entre corchetes []
- Tuplas, tuple: colección ordenadas e inmutable de elementos separados por comas entre paréntesis ()
- Conjuntos, set: colección no ordenada y de elementos distintos separados por comas entre llaves {}
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
students = ['Aitor', 'Alfredo', 'Ary', 'Annie', 'Carlos', 'don Beta', 'Davide', 
            'Fran', 'Irene', 'Matteo B', 'Matteo S', 'Mercedes', 'Pedro']

# recorre la lista students 
#    para ver el nombre de cada estudiante

""" print(len(students), students)
# del students[3]
students.append('Heyson')
students.insert(4, 'David')
print(len(students), students)
 """
months = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'dicienbre')
# print(len(months), type(months), months)

person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

person['age'] = 25
person['city'] = 'Madrid'
for item, value in person.items():
    print(item, value)

del person['email']

# print(len(person), type(person), person)
print(person['email'])  # never: person.email

# del person
person = {}
# print(person)

person = {"first_name": '',
          "last_name": "",
          "email": "",
          'lucky_number': [1, 2, 3]}

person['age'] = 0
person['city'] = '0'

