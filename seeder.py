from tinydb import TinyDB, Query
db = TinyDB('db.json')

db.truncate()

db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'manzana', 'count': 15})
db.insert({'type': 'pera', 'count': 35})
db.insert({'type': 'mandarina', 'count': 100})
db.insert({'type': 'aguacate', 'count': 25})
db.insert({'type': 'uva', 'count': 125})
db.insert({'type': 'nuez', 'count': 1025})


# leo la API de la cual obtengo los datos
# generar la DB (TinyDB)
# grabar registros en la DB
