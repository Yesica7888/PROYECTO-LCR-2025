#from flask import Flask  
#from controllers.main import main 

#app = Flask(__name__)
#app.register_blueprint(main) #registre este archivo porque alli estan las rutas que voy a usar en la app principal es decir aca

#if __name__ == "__main__":
#    app.run (debug=True, port=5000) 

#probando la plantilla

#app = Flask(__name__, template_folder="templates", static_folder="static")
#app.register_blueprint(main)

#if __name__ == "__main__":
#    app.run (debug=True, port=5000, host='0.0.0.0') 

from flask import Flask
import os
from PIL import Image, ImageDraw, ImageFilter
import math
import random

def create_app():
    app = Flask(__name__)
    
    # Función de generación de imágenes (la misma de arriba)
    def generate_test_image():
        width, height = 640, 480
        color = "#FFFFFF"
        
        image = Image.new('RGB', (width, height), color)
        draw = ImageDraw.Draw(image)
        
        for y in range(height):
            for x in range(width):
                transparency_variation = random.randint(250, 255)
                flow_pattern = math.sin(x * 0.02 + y * 0.01) * 2
                
                r = min(255, transparency_variation + flow_pattern)
                g = min(255, transparency_variation + flow_pattern)
                b = min(255, transparency_variation + flow_pattern)
                
                draw.point((x, y), fill=(int(r), int(g), int(b)))
        
        image = image.filter(ImageFilter.SMOOTH_MORE)
        for _ in range(3):
            for y in range(0, height, 20):
                for x in range(0, width, 20):
                    distortion = random.randint(-1, 1)
                    region = image.crop((x, y, x+30, y+30))
                    image.paste(region, (x + distortion, y + distortion))
        
        os.makedirs("static/imgLCR", exist_ok=True)
        image_path = "static/imgLCR/test_lcr.png"
        image.save(image_path)
        print(f"Imagen de prueba generada en: {image_path}")
        return image_path
    
    # Generar imagen al iniciar la app (solo para pruebas)
    print("Generando imagen de prueba...")
    generate_test_image()
    print("Imagen generada. Puedes verla en static/imgLCR/test_lcr.png")
    
    return app

if __name__ == '__main__':
    app = create_app()
    # No ejecutar el servidor web, solo generar la imagen
    # app.run(debug=True)