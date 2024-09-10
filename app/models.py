from datetime import datetime
from .db.db import db


class SliderImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    display = db.Column(db.String(255), nullable=False)


class Subtitle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)


class StoryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    fecha_hora_baja = db.Column(db.DateTime)


class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    bajada = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    fecha_hora_baja = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    images = db.relationship("ImageNews", backref="news", lazy=True)
    video = db.relationship("VideoNews", backref="news", uselist=False)


class ImageNews(db.Model):
    __tablename__ = "image_news"
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey("news.id"), nullable=False)
    path = db.Column(db.String(255), nullable=False)


class VideoNews(db.Model):
    __tablename__ = "video_news"
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(
        db.Integer, db.ForeignKey("news.id"), nullable=False, unique=True
    )
    path = db.Column(db.String(255), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    news = db.relationship("News", backref="author", lazy=True)
    slider_images = db.relationship("SliderImage", backref="user", lazy=True)
    subtitles = db.relationship("Subtitle", backref="user", lazy=True)
    story_images = db.relationship("StoryImage", backref="user", lazy=True)
