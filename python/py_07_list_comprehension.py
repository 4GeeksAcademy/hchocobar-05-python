"""
List Comprehension
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789


Sintaxis:
nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in lista_anterior if condición]

Condicional one liner
valor = verdadero if condición else falso
"""
numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]

duplicate = []
for result in numbers:
    duplicate.append(result * 2)

print(duplicate)

# nueva_lista = [target for item in lista_anterior]
lc_duplicate = [ result * 2 for result in numbers ]
print(lc_duplicate)


# nueva_lista = [target for item in lista_anterior if condición]
if_duplicate = [ result * 2 for result in numbers if result % 2 == 1 ]
print(if_duplicate)