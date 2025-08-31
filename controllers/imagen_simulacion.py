from flask import Blueprint, jsonify
from PIL import Image, ImageDraw, ImageFilter
import os
import math
import random

image_bp = Blueprint('image', __name__)

def generateImg(color="#FFFFFF"): # valor por defecto
    width, height = 640, 480
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)

    # Simulación de transparencia, flujo
    for y in range(height):
        for x in range(width):
            transparency_variation = random.randint(250, 255)
            flow_pattern = math.sin(x * 0.02 + y * 0.01) * 2

            r = min(255, transparency_variation + flow_pattern)
            g = min(255, transparency_variation + flow_pattern)
            b = min(255, transparency_variation + flow_pattern)

            draw.point((x, y), fill=(int(r), int(g), int(b)))

    # Suavizado
    image = image.filter(ImageFilter.SMOOTH_MORE)

    # Distorsiones simuladas
    for _ in range(3):
        for y in range(0, height, 20):
            for x in range(0, width, 20):
                distortion = random.randint(-1, 1)
                region = image.crop((x, y, x + 30, y + 30))
                image.paste(region, (x + distortion, y + distortion))

    # Asegurar directorio
    folder_path = os.path.join("static", "imgLCR")
    os.makedirs(folder_path, exist_ok=True)

    image_path = os.path.join(folder_path, "test_lcr2.png")
    image.save(image_path)

    return image_path

@image_bp.route("/imagen", methods=["GET"]) #debe tener el mismo nombre que el bp generado arriba despues de  las importaciones
def generate_image():
    image_path = generateImg(color="#FFFFFF")  # LCR NORMAL, funcion del controlador imagen_simulacion.py
    return jsonify({"message": "Imagen generada", "path": image_path})