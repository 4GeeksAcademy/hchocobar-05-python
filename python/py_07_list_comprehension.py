"""
List Comprehension
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


Sintaxis:
nueva_lista = [target for row in lista_anterior]
nueva_lista = [target for row in lista_anterior if condición]

Condicional one liner
valor = verdadero if condición else falso
"""
students = ['Agustin', 'Alejandro', 'Anais', 'Bilbo', 'David', 'Gabriela', 'Fidel', 
           'Mar', 'Marco', 'Matias', 'Mery', 'Pablo', 'Pau', 'Robert', 'Victoria', 'Eduardo']

saludos = []
for row in students:
    saludos.append(f'<li>Hola {row}</li<>')

# print(saludos)
# print(students)

greetings = [f'<li>Hola {row}</li<>' for row in students]  # List Compreshions
# print(greetings)

numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]
dobles = [row * 2 for row in numbers]
# print(numbers)

pares = [row for row in numbers if row % 2 == 0 or row == 65]

numeros_pares = []
for row in numbers:
    if row %2 == 0 or row == 65:
        numeros_pares.append(row)


print(numeros_pares)


# condicion = False
number = 800
valor = 'Múltiplo de 5' if number % 5 == 0 else 'No es múltiplo de 5'
print(valor)
