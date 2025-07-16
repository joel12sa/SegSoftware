from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.connection import get_db
from app.squemas.schemas import UsuarioSchema
from app.service.usuario_service import registrar_usuario_service

router = APIRouter()

@router.post("/registro/")
def registrar_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    return registrar_usuario_service(usuario, db)
