from fastapi import FastAPI
from app.db.connection import Base, engine
from app.api.routes_usuarios import router as usuario_router
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_router, prefix="/api", tags=["usuarios"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia por tu dominio para seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)