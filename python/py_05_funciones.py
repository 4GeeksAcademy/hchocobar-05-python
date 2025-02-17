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

# 1. Definir la Función - Declarar
def saludo(year, first_name='Hector', phrase='Bienvenido'):
    pass
    # VErifico que hector e sun usuario activo....... 
    # ..... 
    # print(phrase, first_name, 'hoy es ', DAY_WEEK)
    return f'{phrase} {first_name}, que tengas un exitoso {year:.2f}!'.lower()


def otra_funcion():
    pass
    return


DAY_WEEK = 'Lunes'
numbers = [10, 23, 8, 65, 34, 18, 22, 88, 70]
students = ['Agustin', 'Alejandro', 'Anais', 'Bilbo', 'David', 'Gabriela', 'Fidel', 
           'Mar', 'Marco', 'Matias', 'Mery', 'Pablo', 'Pau', 'Robert', 'Victoria', 'Eduardo']
# 2. Invocarla, ejecutarla, llamarla
name = 'Connor'
foo = saludo(2025, phrase='Hola')
print(foo)
if foo:
    print ('devolvió algo distinto a None')
else:
    print ('No hizo nada')
