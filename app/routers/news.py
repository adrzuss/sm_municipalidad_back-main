from flask import Blueprint, request, jsonify

from app.services import news_service

new_bp = Blueprint("new_api", __name__)


@new_bp.route("/add", methods=["POST"])
def add_new():
    title = request.form.get("title")
    text = request.form.get("text")
    bajada = request.form.get("bajada")
    category = request.form.get("category")
    fechaHora = request.form.get("fechaHora")
    author_id = int(request.form.get("author_id"))
    url = request.form.get("url")
    # Archivos del request
    files = request.files
    id_news = news_service.add_news(
        title, text, bajada, category, fechaHora, author_id, files, url
    )
    new = news_service.get_one_new(id_news)
    return jsonify({"message": "Noticia añadida exitosamente", "data": new}), 200


@new_bp.route("/get", methods=["GET"])
def get_all():
    news = news_service.get_all_news()
    return jsonify({"news": news}), 200


@new_bp.route("/getfour", methods=["GET"])
def get_four():
    news = news_service.get_four_news()
    return jsonify({"news": news}), 200


@new_bp.route("/get/<id>", methods=["GET"])
def get_new(id):
    new = news_service.get_one_new(id)
    if new:
        return jsonify({"new": new}), 200
    else:
        return jsonify({"error": "News not found"}), 404
