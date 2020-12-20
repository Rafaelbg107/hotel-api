from datetime import date, datetime
from typing import Dict
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    idReserva: int = 2
    fechaReserva: datetime = datetime.utcnow()
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

database_reservas = Dict[int, ReservaInDB]
database_reservas = {
    1 : ReservaInDB(**{"idReserva":1,
    "fechaReserva":'2020-12-09 21:30:48.620822',
    "fechaLlegada": '2020-12-10',
    "fechaSalida": '2020-12-12',
    "habitacion": "Suite",
    "numeroPersonas": 2,
    "nombres": "Juan",
    "apellidos": "Rulfo Vizcaíno",
    "email": "juanrulfo@gmail.com",
    "telefono": 3104632378,
    "tipoDocumento": "CC",
    "numeroDocumento": 10227923,
    "pais": "México",
    "ciudad": "San Gabriel",
    "direccion": "Calle 52 #28-20"
    }),

    2 : ReservaInDB(**{"idReserva":2,
    "fechaReserva":'2020-12-09 22:30:48.620822',
    "fechaLlegada": '2020-12-11',
    "fechaSalida": '2020-12-13',
    "habitacion": "Suite",
    "numeroPersonas": 4,
    "nombres": "Gabriel",
    "apellidos": "García Márquez",
    "email": "gabopremionobel@gmail.com",
    "telefono": 3002025632,
    "tipoDocumento": "CC",
    "numeroDocumento": 9845690,
    "pais": "Colombia",
    "ciudad": "Aracataca",
    "direccion": "Calle 1 #2-20"
    })
}
generator = {"id":2} #Auto-Incremental

def save_reserva(reserva_in_db: ReservaInDB):
    generator["id"] = generator["id"] + 1
    reserva_in_db.idReserva = generator["id"]
    reserva_in_db.fechaReserva = datetime.now()
    database_reservas[generator["id"]] =  reserva_in_db
    return reserva_in_db

def get_reserva(idReserva: int):
    if idReserva in database_reservas.keys():
        return database_reservas[idReserva]
    else:
        return None

"""
Se determina si la habitación de un hotel está disponible
según las fechas que ya estén reservadas para esa habitación.
Se comparan las fechas deseadas con cada una de las fechas que ya estén reservadas (for)
El criterio de disponibilidad está dado por la diferencia de las fechas deseadas y reservadas
como una resta punto entre vectores (a,b).-(c,d) = (a-c),(a-d),(b-c),(b-d)
si y sólo si las diferencias son todas positivas o todas negativas es posible reservar.
Es posible reservar con fecha de llegada cuando la habitación se desocupa el mismo día.
De la misma forma, es posible hacerlo si el check-out concide con la fecha de llegada de una
reserva existente. 
"""
def buscar_fecha(reserva_in_db: ReservaInDB):
    fechaLlegadaPref = reserva_in_db.fechaLlegada
    fechaSalidaPref = reserva_in_db.fechaSalida
    salida = True
    for i in database_reservas.values():
      if reserva_in_db.habitacion == i.habitacion:
            fechaLlegadaOcupada = i.fechaLlegada
            fechaSalidaOcupada = i.fechaSalida
            #op1 = fechaLlegadaOcupada - fechaLlegadaPref
            #op2 = fechaLlegadaOcupada - fechaSalidaPref
            #op3 = fechaSalidaOcupada - fechaLlegadaPref
            #op4 = fechaSalidaOcupada - fechaSalidaPref
            a = fechaLlegadaOcupada
            b = fechaSalidaOcupada
            c = fechaLlegadaPref
            d = fechaSalidaPref
            if (a < c) & (a < d) & (b <= c) & (b < d):
                salida = True
            elif (a > c) & (a >= d) & (b > c) & (b > d):
                salida = True
            else:
                return False
    return salida

def get_reservas_usuario(email : str):
    count = 0
    reservas = {}
    for i in reversed(database_reservas.values()):
      if i.email == email:
          count += 1
          reservas["a"+str(count)] = {
            "idReserva":i.idReserva,
            "fechaReserva":i.fechaReserva,
            "fechaLlegada": i.fechaLlegada,
            "fechaSalida": i.fechaSalida,
            "habitacion": i.habitacion,
            "numeroPersonas": i.numeroPersonas,
            "pais": i.pais,
            "ciudad": i.ciudad,
            "direccion": i.direccion
          }
    return reservas
