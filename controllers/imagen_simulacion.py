from flask import Blueprint, jsonify,render_template
from PIL import Image, ImageDraw, ImageFilter
from datetime import datetime 
from models.deteccion import insertDeteccion  #funcion insertar deteccion de modelo
from models.imagen import insertImagen # insertar imagen de acuerdo a la deteccion 
import os
import math
import random

image_bp = Blueprint('image', __name__)
"""
V1 de codigo para generar imagen 

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
    name="test_lcr"
    extension=".png"
    count=1
    image_path = os.path.join(folder_path, name+extension)
    #para que no se sobre escriba la imagen 
    while os.path.exists(image_path):
        image_path=os.path.join(folder_path, f"{name}{count}{extension}")
        count+=1
    image.save(image_path)

    return image_path
"""

def generateImg(color_hex="#FFFFFF",particulas=False, claridad=True, flujo=True ):
    """
    Genera una imagen simulada de líquido con parámetros:
    - color: color base en HEX (ej: "#FFFFFF")
    - flujo: True/False para simular movimiento
    - particulas: True/False para agregar partículas
    - claridez: True/False (True = más clara, False = más turbia)

    -color-particulas-claridad-flujo
    """
    width, height = 640, 480 #dimensiones de la imagen
    image = Image.new('RGB', (width, height), color_hex) # Image metodo de libreria pillow, modo color, dimensiones, color fondo
    draw = ImageDraw.Draw(image) #dibujando imagen metodo ImageDraw de pillow 

    # Variación por flujo px a px
    for y in range(height): #recorrre filas, alto de la img
        for x in range(width): #recorre columnas ancho de la img
            brillo = 240 if claridad else 180  # depende de la claridad se controla el brillo 
            transparencia = random.randint(brillo, 255 if claridad else 200) # transparencia de acuerdo al valor del brillo y claridad
            
            # Si flujo es True, aplica patrón sinusoidal
            flujo = math.sin(x * 0.02 + y * 0.01) * 2 if flujo else 0 #si hay flujo añade patron sen valores entre -2 y +2

            r = min(255, transparencia + flujo) #manteniendo valores hasta 255 que es el limite de color en RGB
            g = min(255, transparencia + flujo)
            b = min(255, transparencia + flujo)
            
            #pintando cada x con el color calgulado
            draw.point((x, y), fill=(int(r), int(g), int(b)))

    # Agregar partículas si está activado
    if particulas:
        num_particulas = 100  # número fijo rango de colores oscuros
        for i in range(num_particulas): #no uso la i
            px = random.randint(0, width - 1)
            py = random.randint(0, height - 1)
            size = random.randint(1, 3) #radio de la particula
            colorParticula = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) #aleatorio r,g,b
            draw.ellipse((px, py, px + size, py + size), fill=colorParticula) #dibujando la particula

    # Ajustar claridez mediante suavizado (si False, imagen más borrosa)
    if not claridad: #claridad FALSE, suaviza para simular falta de nitidez
        for i in range(3):
            image = image.filter(ImageFilter.SMOOTH_MORE)

    # Distorsiones simuladas para movimiento
    for i in range(3):
        for y in range(0, height, 20):
            for x in range(0, width, 20):
                distortion = random.randint(-1, 1)
                region = image.crop((x, y, x + 30, y + 30))
                image.paste(region, (x + distortion, y + distortion))

    # Guardar imagen se le coloca contador para que no se sobreescriba la imagen
    folder_path = os.path.join("static", "imgLCR")
    os.makedirs(folder_path, exist_ok=True)
    name = "test_lcr"
    extension = ".png"
    count = 1
    image_path = os.path.join(folder_path, name + extension)
    while os.path.exists(image_path):
        image_path = os.path.join(folder_path, f"{name}{count}{extension}")
        count += 1
    image.save(image_path)

    #Envio de parametros para realizar la deteccion , tuve que realizar un cast a flujo porque al 
    #generar el flujo queda cmo una variable entera
    parametros_lcr = {"color_hex":color_hex,"particulas":particulas,"claridad":claridad,"flujo":bool(flujo)}

    #envio la ruta de la imagen y los parametros en un diccionario :) para 
    # simular la deteccion, que esta me retorne el id ingresado 
    # y ese id de la deteccion acabado de realizar se envie como parámetro para guardar en la BBDD la imagen 
    return image_path,parametros_lcr


#@image_bp.route("/img") #debe tener el mismo nombre que el bp generado arriba despues de  las importaciones
#def generate_image():
    #image_path = generateImg("#8B0000",True,False,False)  # simulando hemorragia traumatica
    #return jsonify({"message": "Imagen generada", "path": image_path})
    #para mantener el estilo ...

#    image_path,parametros_lcr = generateImg("#8B0000",True,False,False)  

#    return render_template("plantilla/index.html", image_path=image_path, parametros_lcr=parametros_lcr) #le pasa la variable de la imagen


# Parametros de imagen en deteccion, guardando en BBDD una nueva deteccion 

@image_bp.route('/deteccionimg')
def generate_image():
 #generar imagen con parametros
 image_path,parametros_lcr = generateImg("#8B0000",True,False,False)  

 #simular la deteccion y guardar en BBDD
 fecha=datetime.now().date()
 hora=datetime.now().time()
 id_deteccion=insertDeteccion(fecha,parametros_lcr["color_hex"],parametros_lcr["particulas"],
                              parametros_lcr["claridad"],parametros_lcr["flujo"],hora)
#insertando Imagen a la BBDD, recibe como parametro : ruta_imagen,fk_id_deteccion
 id_imagen= insertImagen(image_path,id_deteccion)

 return render_template("plantilla/index.html", image_path=image_path,
                         parametros_lcr=parametros_lcr, deteccion=id_deteccion,
                         imagenbbdd=id_imagen) 
#deteccion es el nombre de la variable que deseo y con ese nombre voy a llamarlo en el index




