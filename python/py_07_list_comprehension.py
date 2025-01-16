"""
List Comprehension
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


Sintaxis:
nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in lista_anterior if condición]

Condicional one liner
valor = verdadero if condición else falso
"""


users = []
users.append('hola')
users.append('ciao')

numbers = []
for i in range(10):
    numbers.append(i)
# print(numbers)

# nueva_lista = [target for item in lista_anterior]
mi_lista = [ i for i in range(10) ]
# print(mi_lista)

students = ['Agustin', 'Alejandro', 'Anais', 'Bilbo', 'David', 'Gabriela', 'Fidel', 
           'Mar', 'Marco', 'Matias', 'Mery', 'Pablo', 'Pau', 'Robert', 'Victoria', 'Eduardo']
saludos = [ f'Hola {item}' for item in students ]
# print(saludos)


# nueva_lista = [target for item in lista_anterior if condición]
all_numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]
even = [ i for i in all_numbers if i % 2 == 0 ]
print(even)
