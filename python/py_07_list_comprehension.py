"""
List Comprehension
https://gist.github.com/hchocobar/d12d31c4ccde8a5f6c318d3eb02f7789

Dict Comprehension

nueva_lista = [target for item in lista_anterior]
nueva_lista = [target for item in <lista_anterior> if <condición>]

Condicional
valor = verdadero if condicion else falso
"""
# nueva_lista = [target for item in lista_anterior]
# nueva_lista = [target for item in <lista_anterior> if <condición>]
def my_function():
  lista = [1, 2 , 3 , 4, 5, 6, 7 , 8, 9]
  results = [item * 2 for item in lista if item % 2 == 0]
  return results


# One linner 
message = [1, 2 , 3 , 4, 5, 6, 7 , 8, 9]
# inicio
results = []
for number in message:
    if number % 2 == 0:
      results.append(number * 2)
print(results)

print(my_function())
