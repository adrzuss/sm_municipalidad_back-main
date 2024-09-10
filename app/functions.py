import base64
from werkzeug.utils import secure_filename
import os
from PIL import Image


def save_file_video(file, folder):
    if file and file.filename:
        filename = secure_filename(file.filename)
        file_path = os.path.join(folder, filename)
        file.save(file_path)
        return file_path
    return None


def save_and_compress_image(file, folder):
    if file and file.filename:
        filename = secure_filename(file.filename)
        file_path = os.path.join(folder, filename)

        file.save(file_path)  # Guardar la imagen original

        compress_image(file_path)  # Comprimir la imagen

        return file_path
    return None


def compress_image(file_path):
    with Image.open(file_path) as img:
        img = img.convert("RGB")  # Asegurar que la imagen esté en formato RGB
        img.save(file_path, "JPEG", optimize=True, quality=85)


def convert_image_to_base64(image_path):
    """Convert image to base64 string."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        return None
