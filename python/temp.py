import so
import sys
from flask import Flask


class TestClass(object):
    
    def class_method1():
        pass

    def class_method2():
        pass


test = TestClass()


def top_level_function1(list_number):
    pass


def top_level_function2():
    pass


students = ['Agustin', 'Alejandro', 'Anais', 'Bilbo', 'David', 'Gabriela', 'Fidel', 
           'Mar', 'Marco', 'Matias', 'Mery', 'Pablo', 'Pau', 'Robert', 'Victoria', 'Eduardo']

months = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
          'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'dicienbre')

person = {"first_name": 'Joe',
          "last_name": "Doe",
          "email": "joe.doe@domain.com"}

numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]


if 25 in numbers:
    print('tengo 25')

# top_level_function1(numbers)
# tratamiento de errores
# asignación multiple de variables
