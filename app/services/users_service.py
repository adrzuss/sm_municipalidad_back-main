from flask import current_app

from sqlalchemy import text

from ..models import User
from ..db.db import db


#TODO Controlar que el usuario no exista
def add_user(usuario, clave, apellido, nombre, documento, telefono, mail, alta, baja):
    user_data = {
        "usuario": usuario,
        "clave": clave,
        "apellido": apellido,
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono,
        "mail": mail,
        "alta": alta,
        "baja": baja
    }

    user = User(**user_data)
    db.session.add(user)
    db.session.commit()

    id_user = user.id
    
    return id_user

def get_one_user(user_id):
    procedure_call = text("CALL GetUserDetails(:users_id)")
    result = db.session.execute(procedure_call, {"user_id": user_id}).mappings().all()

    if not result:
        return None

    first_row = result[0]
    user_data = {
        "id": first_row["user_id"],
        "usuario": first_row["usuario"],
        "clave": first_row["clave"],
        "apellido": first_row["apellido"],
        "nombre": first_row["nombre"],
        "documento": first_row["documento"],
        "telefono": first_row["telefono"],
        "mail": first_row["mail"],
        "alta": first_row["alta"],
        "baja": first_row["baja"]
    }
    
    return user_data

def get_all_users():
    procedure_call = text("CALL GetUsers")
    result = db.session.execute(procedure_call).mappings().all()

    users_all = []
    for row in result:
        user_data = {
            "id": row["user_id"],
            "usuario": row["usuario"],
            "apellido": row["apellido"],
            "nombre": row["nombre"],
            "mail": row["mail"]
        }
        users_all.append(user_data)

    return users_all
