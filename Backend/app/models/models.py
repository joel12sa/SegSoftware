from sqlalchemy import Column, Integer, String, Float, Date
from app.db.connection import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    cedula = Column(String(13), nullable=False, unique=True)
    telefono = Column(String(10), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(String(10), nullable=False)
    direccion = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    sitio_web = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
