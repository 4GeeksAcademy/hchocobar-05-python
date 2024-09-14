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
def saludar(name, saludo='Bienvenido'):
    print(saludo, name)
    return saludo + name

dato = saludar('Héctor')
print('Dato es:', dato)
