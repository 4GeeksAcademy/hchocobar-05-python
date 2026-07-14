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
students = ['Agustin', 'Alejandro', 'Anais', 'Bilbo', 'David', 'Gabriela', 'Fidel', 
            'Mar', 'Marco', 'Matias', 'Mery', 'Pablo', 'Pau', 'Robert', 'Victoria', 'Eduardo']


""" for student in students:
    print(f'hola {student}') """


age = 25
name = 'Héctor'
day = 'Lunes'
text = f'Hola {name}, hoy es {day} cumples {age} años'
text_concatenado = 'Hola ' + name + ', hoy es ' + day + ' cumples ' + str(age) + ' años'
print(text)
print(text_concatenado)

""" 
students[0] = 'Laskmit'
del students[10]
students.append('Héctor')
print(type(students), 'largo de la lista:' ,len(students))
print(students)

 """
""" 
lista = [1, 2, 'hola', True, ['Agustin', 'Alejandro']]
del lista[4]
lista[0] = 100
print(lista) 
"""
""" 
months = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'dicienbre')


months[2] = 'march'
print(months[2])

 """
""" 
canasta = {'uva', 100, 'manzana', 100, 'pera', 100, 'uva', 'pera'}
print(type(canasta))
print(canasta, len(canasta))

lista = ['arg', 'vnz', 'col', 'cr', 'usd', 'vnz', 'usd', 'col']
nacionalidades = set(lista)
print(len(nacionalidades), nacionalidades)
 """


person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com",
          'age': 25,
          'is_active': True}

person['last_name'] = 'Rodriguez'

# print(type(person), len(person))
# print(type(person['age']))
# print(person)
# print(person.keys())
# print(person.values())
# print(person['nombre'])
# print(person.get('first_name', 210))

dict_vacio = {}
# print(type(dict_vacio))


