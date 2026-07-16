"""
Funciones
 - def 
 - Identación y bloques
   - pass
 - argumentos, parámetros
   - argumentos posicionales
   - argumentos por palabra clave
   - mix de argumentos posicionales y palabras clave
   - parámetros con valores por defecto
 - Return / None
 - Alcance (scope) / global / cuidado: sombra
"""

# Defino la función / Declaro 
def custom_function(name, day='día', task='estudiar'):
    global nombre
    texto = f'Hola {name}, hoy es un excelente {day} para {task}'
    nombre = name
    return texto


def fizz_buzz(fin=100):
    for number in range(1, fin + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)
    return 'fin del ejercicio FizzBuzz'


# Invoco la función / llamo la fx / ejecuto la fx
nombre = 'Angélica'
first_name = 'Omar'
result = custom_function('José', task='practicar deportes')

result = fizz_buzz()
print(result)