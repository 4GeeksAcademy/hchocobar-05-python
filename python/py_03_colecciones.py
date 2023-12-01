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

students = ['Andres', 'Alejandro', 'Daniel', 'Evelyn', 'Emiko', 'Guido', 'Leire', 
            'Lorenzo', 'Lourdes', 'Majo', 'Merlina', 'Mike', 'Pau', 'Sara' ,'Yoel']

months = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'dicienbre')

frutas = ['manzana', 'pera', 'uva', 'pera', 'sandia', 'manzana']

frutas_set = set(frutas)
frutas_category = list(frutas_set)

person = {"first_name": 'Joe',
          "last_name": "Doe",
          'age': 25,
          'is_admin': False,
          "email": "joe.doe@domain.com"}

print(students[-3])

# person.first_name

""" for clave, valor in person.items():
  print(valor)
 """
