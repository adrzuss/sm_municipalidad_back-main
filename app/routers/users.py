from flask import Blueprint, request, jsonify
from datetime import date, datetime

from app.services import users_service

user_bp = Blueprint("user_api", __name__)


@user_bp.route("/add", methods=["POST"])
def add_new():
    usuario = request.form.get("usuario")
    clave = request.form.get("clave")
    apellido = request.form.get("apellido")
    nombre = request.form.get("nombre")
    documento = request.form.get("documento")
    telefono = int(request.form.get("telefono"))
    mail = request.form.get("mail")
    alta = date.today()
    baja = datetime.strptime('01/01/1900', '%d/%m/%Y')
    # Archivos del request
    id_user = users_service.add_user(
        usuario, clave, apellido, nombre, documento, telefono, mail, alta, baja
    )
    new = users_service.get_one_user(id_user)
    return jsonify({"message": "Usuario añadido exitosamente", "data": new}), 200


@user_bp.route("/get", methods=["GET"])
def get_all():
    users = users_service.get_all_users()
    return jsonify({"users": users}), 200

@user_bp.route("/get/<id>", methods=["GET"])
def get_new(id):
    user = users_service.get_one_new(id)
    if user:
        return jsonify({"user": user}), 200
    else:
        return jsonify({"error": "Users not found"}), 404
