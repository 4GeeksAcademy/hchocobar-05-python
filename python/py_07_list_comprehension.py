"""
List Comprehension
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


Sintaxis:
nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in lista_anterior if condición]

Condicional one liner
valor = verdadero if condición else falso
"""
numbers = [4, 8, 2, 4, 0, 3]
doble = []
for number in numbers:
    result = number * 2
    doble.append(result)
#  print(doble)
# nueva_lista = [target for item in lista_anterior]
doble_comprehension = [item * 2 for item in numbers]
# nueva_lista = [target for item in lista_anterior if condición]
# doble_compr_if = [item * 2 for item in numbers if item != 3]
print(doble_comprehension)

# double_nums = [num * 2 for num in lib]
# print(double_nums)  # Output: [8, 16, 4, 8, 0, 6]