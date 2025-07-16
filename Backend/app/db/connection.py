from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
# Reemplaza con tus credenciales reales
# Leer variables de entorno
POSTGRES_USER = os.getenv("POSTGRES_USER", "juan")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "usuarios_password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "UsuariosDB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5435")
DB_HOST = os.getenv("DB_HOST", "localhost")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)


# Crea el motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea la clase base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión en endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
