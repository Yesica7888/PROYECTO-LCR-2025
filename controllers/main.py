from flask import Blueprint, render_template
from models.deteccion import getTotalDeteccion  
from models.deteccion_diagnostico import getDetDiaResumen,get_total_riesgo_bajo,get_total_riesgo_alto,get_total_riesgo_moderado #O_O
#para el reporte
from reportlab.pdfgen import canvas
from controllers.diagnostico_simulacion import NOMBRESCOLORES #para el forms
import os

main= Blueprint('main', __name__ )

@main.route('/principal')   
def index(): #con este nombre se llama en el index.html
    totalDetecciones= getTotalDeteccion() #total detecciones 
    # detecciones por riesgo
    riesgo_bajo= get_total_riesgo_bajo()
    riesgo_moderado = get_total_riesgo_moderado()
    riesgo_alto = get_total_riesgo_alto()

    return render_template ("plantilla/index.html", resultado=totalDetecciones, 
                            r1=riesgo_bajo,r2=riesgo_moderado,r3=riesgo_alto) #de la carpeta templates accede al index


@main.route('/detalle/<tipo>')
def detalle(tipo):
    if tipo == "1":
        return f"Total de detecciones: {getTotalDeteccion()}"
    if tipo == "2":
        return f"Riesgo bajo: {get_total_riesgo_bajo()}"
    if tipo == "3":
        return f"Riesgo moderado: {get_total_riesgo_moderado()}"
    if tipo == "4":
        return f"Riesgo alto: {get_total_riesgo_alto()}"
    
    return "Detalle no encontrado."



#blueprint para otra pag
@main.route('/graficos')
def graficos():
    return render_template('plantilla/charts.html')

#blueprint para otra pag, pendiente crear en controlador un archivo por bp 
@main.route('/simulacion')
def simular_img():
   return render_template('plantilla/simulacion-img.html', colores_formulario=NOMBRESCOLORES)

#detecciones tabla detallada
@main.route('/detecciones')
def detecciones():
    # Tabla de resumen  
    columns,registros= getDetDiaResumen()
    print("Columns:", columns)
    print("Registros:", type(registros), len(registros))
    return render_template('plantilla/deteccion.html',titulos=columns,registros=registros,)


@main.route('/reportepdf')
def reporte():
    # Ruta del archivo PDF
    nombre_archivo = "reporte.pdf"
    path = os.path.join("static", "reportes", nombre_archivo)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Crear PDF básico si no existe
    if not os.path.exists(path):
        c = canvas.Canvas(path)
        c.drawString(100, 750, "PDF vacío de prueba")
        c.save()

    # Renderizar la plantilla HTML del visor
    return render_template('plantilla/reporte-pdf.html', pdf_file=nombre_archivo)
 

   

 

    



