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
def saludo(saludo='Buenas', name='Hector', tiempo='mañana'):
    print(saludo, tiempo, name)
    return

saludo(tiempo='noches')