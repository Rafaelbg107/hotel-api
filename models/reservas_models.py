from pydantic import BaseModel
from datetime import datetime, date

class ReservaIn(BaseModel):
    idReserva: int
    fechaReserva: datetime
    fechaLlegada: date
    fechaSalida: date
    habitacion: str
    numeroPersonas: int
    nombres: str
    apellidos: str
    email: str
    telefono: int
    tipoDocumento: str
    numeroDocumento: int
    pais: str
    ciudad: str
    direccion: str

class ReservaOut(BaseModel):
    idReserva: int
    fechaReserva: datetime
    fechaLlegada: date
    fechaSalida: date
    habitacion: str
    numeroPersonas: int
    nombres: str
    apellidos: str
    email: str
    telefono: int
    tipoDocumento: str
    numeroDocumento: int
    pais: str
    ciudad: str
    direccion: str