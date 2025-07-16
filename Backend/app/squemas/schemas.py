from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date
import re

class UsuarioSchema(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30, pattern=r'^[A-Za-z]+$')
    apellido: str = Field(..., min_length=3, max_length=30, pattern=r'^[A-Za-z]+$')
    cedula: str = Field(..., pattern=r'^\d{10}(\d{3})?$')  # 10 o 13 dígitos
    telefono: str = Field(..., min_length=10, max_length=10, pattern=r'^\d{10}$')
    fecha_nacimiento: date
    genero: str = Field(..., min_length=1)
    direccion: str = Field(..., max_length=20)
    salario: float = Field(..., ge=470, le=5000)
    email: EmailStr
    sitio_web: str
    password: str = Field(..., min_length=8, max_length=12)

    @validator("fecha_nacimiento")
    def validar_fecha(cls, v):
        if v < date(1900, 1, 1) or v > date.today():
            raise ValueError("Fecha fuera de rango válido")
        return v

    @validator("direccion")
    def validar_direccion(cls, v):
        if re.search(r'[<>{};]', v):
            raise ValueError("La dirección contiene caracteres no permitidos")
        return v

    @validator("cedula")
    def validar_cedula_ecuatoriana(cls, v):
        if not v.isdigit() or len(v) < 10:
            raise ValueError("La cédula debe contener al menos 10 dígitos numéricos")

        cedula = v[:10]
        provincia = int(cedula[:2])
        tercer_digito = int(cedula[2])

        if provincia < 1 or provincia > 24:
            raise ValueError("Código de provincia inválido en la cédula")
        if tercer_digito >= 6:
            raise ValueError("El tercer dígito no corresponde a una persona natural")

        total = 0
        for i in range(9):
            digito = int(cedula[i])
            if i % 2 == 0:  # posiciones impares (0,2,4,...)
                mult = digito * 2
                if mult > 9:
                    mult -= 9
                total += mult
            else:
                total += digito

        verificador = (10 - (total % 10)) % 10
        if verificador != int(cedula[9]):
            raise ValueError("Cédula inválida según el dígito verificador")

        return v
