from pydantic import BaseModel


class UsuariosIn(BaseModel):
    email: str
    clave: str 

class UsuariosOut(BaseModel):
    email: str
    nombres: str
    apellidos: str
    telefono: int
    pais: str
    ciudad: str
    direccion: str