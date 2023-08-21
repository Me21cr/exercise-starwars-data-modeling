import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    characters_id= Column(Integer, ForeignKey('characters.id'), nullable=True)
    planets_id= Column(Integer, ForeignKey('planets.id'), nullable=True)
    
    
class Usuario(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column (String(250), nullable=False)
    email= Column (String(100), nullable=False)
    username= Column (String(100), nullable=False)
    age= Column(Integer, nullable=False)
    favorites= relationship(Favorites, backref= "user")


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column (String(20), nullable=False)
    eyes_color= Column (String(20), nullable=True)
    age= Column(Integer, nullable=False)
    birth_year= Column(Integer, nullable=False)
    favorites= relationship(Favorites, backref= "characters")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column (String(250), nullable=False)
    terrain= Column (Integer, nullable=False)
    height= Column (Integer, nullable=False)
    climate= Column (String(250), nullable=False)
    diameter= Column (Integer, nullable=False)
    favorites= relationship(Favorites, backref= "planets")


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')