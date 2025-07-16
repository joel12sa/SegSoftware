from sqlalchemy.orm import Session
from app.squemas.schemas import UsuarioSchema
from app.repositories.usuario_repository import (
    obtener_usuario_por_cedula_o_email,
    crear_usuario
)
from fastapi import HTTPException
from passlib.context import CryptContext  # Importa CryptContext para el hashing

# Configura el contexto de hashing (usa bcrypt por defecto)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def registrar_usuario_service(usuario: UsuarioSchema, db: Session):
    # Verifica si el usuario ya existe
    existente = obtener_usuario_por_cedula_o_email(db, usuario.cedula, usuario.email)
    if existente:
        raise HTTPException(status_code=400, detail="Cédula o email ya registrados")

    # Hashea la contraseña antes de guardarla
    hashed_password = pwd_context.hash(usuario.password)
    usuario.password = hashed_password  # Reemplaza la contraseña en texto plano

    # Crea el usuario con la contraseña hasheada
    usuario_nuevo = crear_usuario(db, usuario)
    return {"mensaje": "Usuario registrado exitosamente", "usuario_id": usuario_nuevo.id}