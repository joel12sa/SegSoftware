from sqlalchemy.orm import Session
from app.models.models import Usuario
from app.squemas.schemas import UsuarioSchema

def obtener_usuario_por_cedula_o_email(db: Session, cedula: str, email: str):
    return db.query(Usuario).filter((Usuario.cedula == cedula) | (Usuario.email == email)).first()

def crear_usuario(db: Session, usuario: UsuarioSchema):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario
