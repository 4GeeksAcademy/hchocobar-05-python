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

def welcome(saludo, name):
    print(saludo, name)
    name = 'Alvaro'
    print(name)


name = 'Hector'
welcome('hola', name)
print(name)
