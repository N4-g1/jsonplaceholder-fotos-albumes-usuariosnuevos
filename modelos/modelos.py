from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    correo = Column(String(255), nullable=False)
    contrasena_hash = Column(String(255), nullable=False)

class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    userId = Column(Integer)  


    fotos = relationship("Foto", back_populates="album", cascade="all, delete-orphan")

class Foto(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    url = Column(String(500), nullable=False)
    thumbnailUrl = Column(String(500), nullable=False)
    albumId = Column(Integer, ForeignKey('albums.id'))
    
    
    album = relationship("Album", back_populates="fotos")

