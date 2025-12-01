"""
Porque Python
1989 - Guido Van Rossum
• Es fácil de utilizar.
• Es un lenguaje “completo”; no sirve sólo para programar scripts.
• Tiene gran variedad de estructuras de datos incorporadas al propio lenguaje.
• Tiene una gran cantidad de bibliotecas (libraries). PyPi
• Permite la 
    ◦ programación modular, 
    ◦ orientada a objetos y su uso 
    ◦ como un lenguaje imperativo tradicional.
• Es interpretado. Esto facilita el desarrollo (aunque ralentice la ejecución).
• Se puede utilizar desde un entorno interactivo.
• Se puede extender fácilmente.
• Es muy expresivo: un programa Python ocupa mucho menos que su equivalente en otros lenguajes.

"""

first_name = 'Joe'  # Nombre
last_name = 'Doe'   # Apellido
age = 25  # Edad
# age = 25

numero = 50
if numero < 100:
    letra = 'a'
    palabra = 'hola'
    multi_letra = letra * 5
    print('Hola')
elif numero < 200:
    print('Chao')
else:
    print('Adiós')

user = ''
for char in 'john.smith@pythoninstitute.org':
    if char == '@':
        break
    user += char
print(user)  # Salida: 'john.smith'


# Listas
ordinales = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto', 
             'sexto', 'séptimo', 'octavo', 'noveno', 'décimo'] 


# Tuplas
dias = ('lunes', 
        'martes', 
        'miércoles', 
        'jueves', 
        'viernes', 
        'sábado', 
        'domingo')
meses = ('enero', 
         'febrero', 
         'marzo', 
         'abril', 
         'mayo', 
         'junio', 
         'julio', 
         'agosto', 
         'setiembre', 
         'octubre', 
         'noviembre', 
         'diciembre')
# Diccionarios
usuario = {'nombre': 'Jane Doe',
           'edad': 23,
           'curso': 'Curso de Python',
           'skills': {'programación': True,
                      'base_de_datos': False},
           'niveles': ['básico', 'intermedio']}


usuario = {
    'nombre': 'Jane Doe',
    'edad': 23,
    'curso': 'Curso de Python',
    'skills': {
        'programación': True,
        'base_de_datos': False
    },
    'niveles': [
        'básico', 
        'intermedio'
    ]
}

figure.update_layout(title='Selección del mejor K', 
                     xaxis_title='Valor de K',
yaxis_title='Precisión promedio', xaxis=dict(dtick=1),
                     template='plotly_white', width=800, height=500)
