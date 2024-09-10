from flask import current_app
from sqlalchemy import text

from app.functions import convert_image_to_base64, save_and_compress_image
from ..models import SliderImage, Subtitle, StoryImage
from ..db.db import db


# SLIDER
def add_slider_image(author_id, files, display):
    upload_folder = current_app.config["UPLOAD_FOLDER"]

    for key in files:
        if "image" in key:
            file = files[key]
            image_path = save_and_compress_image(file, upload_folder)

            if not image_path:
                raise ValueError("Failed to save image")

            if image_path:
                img_n = {
                    "image_url": image_path,
                    "file_name": file.filename,
                    "author_id": author_id,
                    "display": display,
                }
                new_slider_img = SliderImage(**img_n)

                try:
                    db.session.add(new_slider_img)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    raise ValueError(f"Database error: {str(e)}")
    return True


def get_slider_image(display):
    procedure_call = text("CALL GetSliderImages(:display)")
    result = db.session.execute(procedure_call, {"display": display}).mappings().all()

    if not result:
        return None

    slider = []
    for row in result:
        image_path = row["image_path"]
        # image_base64 = convert_image_to_base64(image_path) if image_path else None

        slider_data = {
            "id": row["slider_id"],
            "image": row["image_path"],
            "file_name": row["file_name"],
        }
        slider.append(slider_data)

    return slider


# SUBTITLE
def add_subtitle(author_id, text):
    subtitle = {"text": text, "author_id": author_id}
    new_subtitle = Subtitle(**subtitle)
    db.session.add(new_subtitle)
    db.session.commit()


def get_subtitle():
    procedure_call = text("CALL GetSubtitle")
    result = db.session.execute(procedure_call).mappings().all()
    row = result[0]
    return row["text"]


# HISTORIA
def add_story(file, file_name, author_id, fecha_hora_baja):
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    path = save_and_compress_image(file, upload_folder)
    story = {
        "image_url": path,
        "file_name": file_name,
        "author_id": author_id,
        "fecha_hora_baja": fecha_hora_baja,
    }
    newStory = StoryImage(**story)
    db.session.add(newStory)
    db.session.commit()


def get_story():
    procedure_call = text("CALL GetStory")
    result = db.session.execute(procedure_call).mappings().all()

    if not result:
        return None

    story_list = []
    for story_item in result:
        story_data = {
            "id": story_item["id"],
            "image_url": story_item["image_url"],
            "file_name": story_item["file_name"],
        }
        story_list.append(story_data)
    return story_list
