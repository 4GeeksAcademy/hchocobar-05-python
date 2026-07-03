"""
List Comprehension
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


Sintaxis:
nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in lista_anterior if condición]

Condicional one liner
valor = verdadero if condición else falso
"""


lista = ['Antony', 'Alberto', 'Pedro']

""" 
results = []
for row in lista:
    results.append(f'Bienvenido {row}')
 """

# List Comprehension (one-liner)
results = [f'Bienvenido {row}' for row in lista]

# print(results)

numbers = range(10)
for number in numbers:
    print(number)

duplicados = [number * 2 for number in numbers if number % 3 != 0]
print(duplicados)
