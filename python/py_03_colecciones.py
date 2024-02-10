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

Tips diccionarios
- método .get()  # deveulve el valor de la clave del argumento o None si no existe.
- método .items()  # devuelve el par 'clave': valor y nos permite desempaquetar
- operador in  # para verificar si una clave existe en un diccionario
"""
message = 'Bienvenido!' # Variable string
students = ['Aitor', 'Elisa', 'Alfredo', 'Ary', 'Annie', 'Carlos', 'don Beta', 'Davide', 
            'Fran', 'Irene', 'Matteo B', 'Matteo S', 'Mercedes', 'Pedro']
# print(type(students[5]), students[5])
# del students[2]
# print(students)

months = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'dicienbre')

# names = ['Juan', 'Joe', 'Jimy', 'Juan', 'Jael', 'Juan']
unique_name = {'Juan', 'Joe', 'Jimy', 'Juan', 'Jael', 'Juan'}

person = {"first_name": 'Joe',
          "last_name": "Doe",
          'city': 'New York',
          'age': 25,
          'sports': ['golf', 'rugby', 'soccer'],
          "email": "joe.doe@domain.com"}

professors = {}

person['places'] = ['Madrid', 'Sevilla']


students.append('Elisa')
print(students)
# print(person['ciudad'])
# print(person.get('ciudad'))
