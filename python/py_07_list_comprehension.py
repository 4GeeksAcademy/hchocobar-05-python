"""
List Comprehension
Documentación: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


Dict Comprehension

nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in <lista_anterior> if <condición>]
valor = verdadero if condicion else falso
"""
students = ['Andres', 'Alejandro', 'Daniel', 'Evelyn', 'Emiko', 'Guido', 'Leire', 
           'Lorenzo', 'Lourdes', 'Majo', 'Merlina', 'Mike', 'Pau', 'Sara' ,'Yoel']


saludos = ['Hola ' + item for item in students]
numbers = [1, 2, 12, 57, 45, 79, 30]

numbers_filter = [item for item in numbers if item < 32]

person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

valor = person['first_name'] if person.get('first_name') else 'No tien clave name'
print(valor)