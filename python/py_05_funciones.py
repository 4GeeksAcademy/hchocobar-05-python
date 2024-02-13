"""
Funciones
  - Declaración vs Invocación (ejecución)
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
  - PEP8 - Layout Siempre defimos las Clases y las funciones primero
    - A menos que la variable sea una instancia de una clase
"""
def my_function(person, message, deseo='Que tengas un lindo día'):
    # name es una sombra
    print('dentro de la funcion', person)
    name = 'Elisa'
    print(name)
    return 'funciona'


lista = [1, 2, 3]
name = 'Hector'
my_function(name, 'Buen día')  # Envio argumentos que son valores
valor = my_function('Elisa', 'Bueas tardes')
print('fuera de la funcion pero luego de la funcion', name)
print(valor)
