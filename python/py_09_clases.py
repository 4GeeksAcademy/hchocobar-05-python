"""
Programación Orientada a Objetos 

Clases
- Nombres de clases en CapCase - CapitalizedCase
- Las clases tiene dos tipos de atributos
  - atributos de datos
  - atributos de métodos 
- Argumento self - apuntando a mi mismo (a la propia clase)
- Función repr()
"""

class Dog:
    def __init__(self, name, alfa):
        self.name = name
        self.alfa = alfa
        self.trucos = []

    def add_trucos(self, truco):
        self.trucos.append(truco)

    def __repr__(self):
        return f'<Dog: {self.name} es de {self.alfa}>'


toby = Dog('Toby', 'Mike')  # toby es una instancia de la clase Dog
toby.add_trucos('Se hace el muerto')
toby.add_trucos('Salta')
print(toby.alfa)
print(toby.trucos)

romeo = Dog('Romeo', 'Majo')
romeo.add_trucos('Se hace el muerto')
print(romeo.alfa)
print(romeo.trucos)

print(toby)
print(romeo)

