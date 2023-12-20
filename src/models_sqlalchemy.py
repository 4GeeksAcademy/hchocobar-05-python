"""
Modelado: SQLAlchemy
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


# Creamos la instancia de Base
Base = declarative_base()


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    # 3. Relaciones. relationship(Models)
    # 4. Métodos 


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String, nullable=False)
    subscrition_date  = Column(Date, nullable=False)


class Addresses(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class Profiles(Base):
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    __tablename__ = 'profiles'
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    firstname = Column(String(20))
    lastname = Column(String(20))
    nickname = Column(String(20))
    image_url = Column(String(120))
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    users_id = Column(Integer, ForeignKey('users.id'), unique=True)
    # 3. Relaciones. relationship(Models)
    users = relationship(Users)


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class Characters(Base):
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    __tablename__ = 'characters'
    # 2. Columnas
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    name = Column(String(100), nullable=False)
    description = Column(String(250), nullable=False)
    height = Column(String, nullable=False)
    mass = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    homeworld = Column(String, nullable=False)
    url = Column(String, nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250), nullable=False)
    diameter = Column(String, nullable=False)
    rotation_period = Column(String, nullable=False)
    orbital_period = Column(String, nullable=False)
    gravity = Column(String, nullable=False)
    population = Column(String, nullable=False)
    climate = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    surface_water = Column(String, nullable=False)
    url = Column(String, nullable=False)


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class FavoriteCharacters(Base):
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    __tablename__ = 'favorite_characters'
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    id = Column(Integer, primary_key=True)
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    users_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer,  ForeignKey('characters.id'))
    # 3. Relaciones. relationship(Models)
    users = relationship(Users)
    characters =relationship(Characters)
    # 4. Métodos 


# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    users = relationship(Users)
    planets = relationship(Planets)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
