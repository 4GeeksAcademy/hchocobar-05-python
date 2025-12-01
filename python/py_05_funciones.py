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
def saludo(name='Héctor', text='Hola'):
    result = f'{text} {name}, este es el saludo'
    return result


foo = saludo()
print(foo)
