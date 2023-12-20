"""
Modelado: Flask_SQLAlchemy
# Creamos una class que será el Modelo instanciando de (db.Model) Naming convention: PascalCase en plural
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    # 3. Relaciones. relationship(Models)
    # 4. Métodos 
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db. db.String(120), unique=True, nullable=False)
    password = db.Column(db. db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    subscrition_date  = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        # do not serialize the password, its a security breach
        return {"id": self.id,
                "email": self.email}


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column( db.String(100), nullable=False)
    description = db.Column( db.String(250), nullable=False)
    height = db.Column( db.String, nullable=False)
    mass = db.Column( db.String, nullable=False)
    hair_color = db.Column( db.String, nullable=False)
    skin_color = db.Column( db.String, nullable=False)
    eye_color = db.Column( db.String, nullable=False)
    birth_year = db.Column( db.String, nullable=False)
    gender = db.Column( db.String, nullable=False)
    homeworld = db.Column( db.String, nullable=False)
    url = db.Column( db.String, nullable=False)


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String, nullable=False)
    mass = db.Column(db.String, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    homeworld = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)


class FavoriteCharacters(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    characters_id = db.Column(db.Integer,  db.ForeignKey('characters.id'))
    users = db.relationship(Users)
    characters =db.relationship(Characters)


class FavoritePlanets(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    users = db.relationship(Users)
    planets = db.relationship(Planets)
