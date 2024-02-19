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
   - Siempre una funcion devuelve algo.
     - Si no tengo un return devuelve None
     - Si tengo un return sin nada, devuelve None
     - Si tengo un return con algo, devuelve algo
 - Alcance (scope) / global / cuidado: sombra
"""

# Declaro una función
def saludo(name, saludo='Buen día'):
    # print(saludo, name)
    # return saludo + ', ' + name + '!'
    return f'{saludo}, {name}!'

# Invoco o ejecuto mi función
text = saludo('Susana')
print(text)
