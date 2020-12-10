from typing import Dict
from pydantic import BaseModel

class UsuariosInDB(BaseModel):
    email: str
    nombres: str
    apellidos: str
    telefono: int
    tipoDocumento: str
    numeroDocumento: int
    pais: str
    ciudad: str
    direccion: str
    clave: str 

database_usuarios = Dict[str, UsuariosInDB]
database_usuarios = {
    "juanrulfo@gmail.com" : UsuariosInDB(**{
                            "email": "juanrulfo@gmail.com",
                            "clave": "pedroparamo",
                            "nombres": "Juan",
                            "apellidos": "Rulfo Vizcaíno",
                            "telefono": 3104632378,
                            "tipoDocumento": "CC",
                            "numeroDocumento": 10227923,
                            "pais": "México",
                            "ciudad": "San Gabriel",
                            "direccion": "Calle 52 #28-20"}),
                            
    
    "pepitoperez@gmail.com" : UsuariosInDB(**{
                            "email": "pepitoperez@gmail.com",
                            "clave": "pepeperez",
                            "nombres": "Pedro Pablo",
                            "apellidos": "Perez Gonzalez",
                            "telefono": 3196747556,
                            "tipoDocumento": "CC",
                            "numeroDocumento": 1019589623,
                            "pais": "Colombia",
                            "ciudad": "Barranquilla",
                            "direccion": "Calle 13 #17-06"
                            })
                        }
    
 
def get_usuarios(email: str):
    if email in database_usuarios.keys():
        return database_usuarios[email]
    else:
        return None

def update_usuarios(usuarios_in_db: UsuariosInDB):
    database_usuarios[usuarios_in_db.email] = usuarios_in_db
    return usuarios_in_db

