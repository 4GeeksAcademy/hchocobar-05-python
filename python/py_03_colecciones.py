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


my_lista = [1, 2, 5, 'hoy', True]
colection = (1, 2, 5, 'hoy', True)
my_tupla = (1, 2, 5, 'hoy', True)
# print(colection[0], type(colection))
# print(type(colection[0]))

# print(my_lista)
my_lista[0] = 100
my_lista.append('elemento')

# print(my_lista)
# print(len(my_lista))

""" print(my_tupla)
my_tupla[0] = 100
print(my_tupla) """

conjunto = {1, 20, 30, 'manzana', 20, 'manzana'}
# print(conjunto)
conjunto_vacio = set()
# print(conjunto_vacio, type(conjunto_vacio))


diccionario = {'name': 'Hector',
               'lastname': 'Chocobar',
               'age': 45,
               'married': True,
               'sports': ['soccer', 'rugby', 'golf'],
               'location': {'lat': 32,
                            'long': 4}}
# diccionario = dict()
# print(diccionario)
# print(diccionario['locatio'])
# print(diccionario['nombre'])
# print(diccionario.get('nombre', 'Nombre no definido'))
# print(diccionario.keys())

# print(diccionario.items())

lista_de_elementos_de_un_diccionario = diccionario.items()
print(lista_de_elementos_de_un_diccionario)

for foo, bar in diccionario.items():
    print(f'{foo}     tiene el valor: {bar}')

