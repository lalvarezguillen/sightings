'''
ORMs
'''
from uuid import uuid4
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


BASE = declarative_base()


class Individuo(BASE):
    '''
    Representa un individuo avistado
    '''
    __tablename__ = 'individuo'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    nombre = Column(String(250), nullable=False)
    avistamientos = relationship("Avistamiento", back_populates="avistados")


class Avistamiento(BASE):
    '''
    Representa eventos de avistamiento de individuos
    '''
    __tablename__ = 'avistamiento'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    longitud = Column(Float, nullable=False)
    latitud = Column(Float, nullable=False)
    individuo_id = Column(String(36), ForeignKey('individuo.id'))
    avistados = relationship("Individuo", back_populates="avistamientos")


ENGINE = create_engine('sqlite://')


BASE.metadata.create_all(ENGINE)
