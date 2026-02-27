from flask import Blueprint,render_template, request, redirect, url_for, session
from PIL import Image, ImageDraw, ImageFilter
from datetime import datetime 
from models.deteccion import insertDeteccion  #funcion insertar deteccion de modelo
from models.imagen import insertImagen # insertar imagen de acuerdo a la deteccion 
from controllers.diagnostico_simulacion import analisisDeteccion 
from controllers.diagnostico_simulacion import NOMBRESCOLORES #para el forms
import os
import math
import random

image_bp = Blueprint('image', __name__)


#--- GET formulario (vacio)---
@image_bp.route('/simulacion')
def simular_img():
    
    resultado = session.pop('resultado_simulacion', None)  # cuando entra aca o f5 no duplica la deteccion
    image= session.pop('image_path', None)
    
   # estoy enviando los nombres de los colores como colores_formulario
    return render_template('plantilla/simulacion-img.html', colores_formulario=NOMBRESCOLORES, res_form=resultado, imagen_form=image) 

#--- POST al hacer clic en simular --- 
@image_bp.route('/deteccionimg', methods=['POST'])
def generate_image():
    try:
        #parametros del formulario          
        color=request.form.get('color')
        particulas=request.form.get('particulas')== "true"
        claridad=request.form.get('claridad') == "true"
        flujo=request.form.get('flujo') == "true"

        #generación de imagen y retorno de ruta
        image_path = generateImg(color,particulas,claridad,flujo) 

        #simular la deteccion y guardar en BBDD
        fecha=datetime.now().date()
        hora=datetime.now().time()
        id_deteccion= insertDeteccion(fecha,color,particulas,claridad,flujo,hora)

         #insertar la Imagen a la BBDD recibe como parametro : ruta_imagen,fk_id_deteccion
   
        id_imagen= insertImagen(image_path,id_deteccion)
        
         #Realizando el diagnostico 
        id_diag_det,diagnostico = analisisDeteccion(id_deteccion) #le envio el id de la deteccion y devuelve el id de la asociacion del diagnostico con la deteccion 
        
        # Variable de sesion de imagen independiente
        session['image_path'] = image_path
        #---Guardando el resto de variables en el diccionario----
        session['resultado_simulacion'] = {
           "deteccion":id_deteccion,
           "imagenbbdd":id_imagen,
           "deteccion_diagnostico":id_diag_det,
           "diagnostico":diagnostico[1]            
        }
        
         #---Redirect, asi no se reenvia el POST. nombre del bp + nombre de funcion
        return redirect(url_for('image.simular_img'))
     
    except Exception as e:
        return render_template("plantilla/error.html", error=str(e)), 500
    
def generateImg(color_hex="#FFFFFF",particulas=False, claridad=True, flujo=True ):
    
    width, height = 640, 480 #dimensiones de la imagen
    image = Image.new('RGB', (width, height), color_hex) # Image metodo de libreria pillow, modo color, dimensiones, color fondo
    draw = ImageDraw.Draw(image) #dibujando imagen metodo ImageDraw de pillow 

    # Variación por flujo px a px
    for y in range(height): #recorrre filas, alto de la img
        for x in range(width): #recorre columnas ancho de la img
            brillo = 240 if claridad else 180  # depende de la claridad se controla el brillo 
            transparencia = random.randint(brillo, 255 if claridad else 200) # transparencia de acuerdo al valor del brillo y claridad
            
            # Si flujo es True, aplica patrón sinusoidal
            
            flujo_px = math.sin(x * 0.02 + y * 0.01) * 2 if flujo else 0 #si hay flujo añade patron sen valores entre -2 y +2

            r = min(255, transparencia + flujo_px) #manteniendo valores hasta 255 que es el limite de color en RGB
            g = min(255, transparencia + flujo_px)
            b = min(255, transparencia + flujo_px)
            
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
    # se guarda la imagen de acuerdo a SO         
    image.save(image_path)

    #Si el SO es windows debo normalizar todo porque queda guardado con backslash

    image_path_web = image_path.replace("\\", "/").replace("static/", "")

    print(" Ruta completa guardada en disco:", image_path)
    print(" Ruta normalizada para web (guardada en BBDD):", image_path_web)
    return image_path_web



    
   