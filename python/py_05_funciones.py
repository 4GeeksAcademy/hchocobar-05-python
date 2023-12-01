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

def my_function(dia, mensaje, name, exclamacion='Diviertete!'):
    """
    Ayuda para mi funcion de Argumentos y parametros
      dia: str, un dia de la semana
      mensaje: str, Un mensaje way
      name: str, Nombre propio
    """
    print('hola', name, mensaje, 'Feliz', dia, exclamacion)


my_function('viernes', name='Hector', mensaje='Bienvenido!', exclamacion='A dormir')


