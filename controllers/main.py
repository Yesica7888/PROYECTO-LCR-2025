from flask import Blueprint, render_template, jsonify
from models.deteccion import getTotalDeteccion,get_total_sindiagnostico  
from models.deteccion_diagnostico import getDetDiaResumen,get_total_riesgo_bajo,get_total_riesgo_alto,get_total_riesgo_moderado,get_total_por_diagnostico
import models.deteccion_diagnostico as dd #para no escribir todas las funciones del modelo
from reportlab.pdfgen import canvas #reporte PDF
import os

main= Blueprint('main', __name__ )


#-----------Pagina principal---------------

@main.route('/principal')   
def index(): #con este nombre se llama en el index.html
    totalDetecciones= getTotalDeteccion() #total detecciones 
    # detecciones por riesgo
    riesgo_bajo= get_total_riesgo_bajo()
    riesgo_moderado = get_total_riesgo_moderado()
    riesgo_alto = get_total_riesgo_alto()
    sin_diagnostico= get_total_sindiagnostico()
    
    #Variables para diagrama de barras en detalle de los card
  
    return render_template ("plantilla/index.html", resultado=totalDetecciones, 
                            r1=riesgo_bajo,r2=riesgo_moderado,r3=riesgo_alto,r4=sin_diagnostico) #de la carpeta templates accede al index


#----Función para detalle de los card , resumen de la información requerida 
@main.route('/detalle/<tipo>')
def detalle(tipo):
    if tipo == "1":
        registros=get_total_por_diagnostico()
        diagnostico = []
        total= []
        if registros:
            diagnostico=[d[0] for d in registros]
            total=[t[1] for t in registros]
        return jsonify({
        "mensaje": f"Total de detecciones ruta detalle tipo: {getTotalDeteccion()}",
        "diagnosticos": diagnostico,
        "total": total
    })
         
    if tipo == "2":
        registros=dd.get_diagnosticos_riesgo_bajo()
        diagnostico = []
        total= []
        if registros:
            diagnostico=[d[0] for d in registros]
            total=[t[1] for t in registros]       
        return jsonify({
            "mensaje" : f"Riesgo bajo: {get_total_riesgo_bajo()}" ,
            "diagnosticos": diagnostico,
            "total": total
            })
    if tipo == "3":
        registros=dd.get_diagnosticos_riesgo_moderado()
        diagnostico = []
        total= []
        if registros:
            diagnostico=[d[0] for d in registros]
            total=[t[1] for t in registros]  
        return jsonify({
            "mensaje" : f"Riesgo moderado: {get_total_riesgo_moderado()}",
            "diagnosticos": diagnostico,
            "total": total
            })
    if tipo == "4":
        registros=dd.get_diagnosticos_riesgo_alto()
        diagnostico = []
        total= []
        return jsonify({
            "mensaje": f"Riesgo alto: {get_total_riesgo_alto()}",
            "diagnosticos": diagnostico,
            "total": total  
            })
    if tipo == "5":
        registros=dd.get_sin_diagnostico()
        diagnostico = []
        total= []
        return jsonify({
            "mensaje": f"Sin detección: {get_total_sindiagnostico()}",
            "diagnosticos": diagnostico,
            "total": total 
        })
    
    return jsonify({"error": "Detalle no encontrado"}), 400






#----------blueprint diagrama circular de los diagnosticos--------
@main.route('/graficos')
def graficos():
    registros=get_total_por_diagnostico()
    diagnostico = []
    total_diagnostico = []
    if registros:
       diagnostico = [d[0] for d in registros]
       total_diagnostico= [t[1] for t in registros]
    return render_template('plantilla/charts.html', diagnosticos=diagnostico, total=total_diagnostico)

#-----------Detecciones tabla detallada-------------
@main.route('/detecciones')
def detecciones():
    # Tabla de resumen  
    columns,registros= getDetDiaResumen()
    #print("Columns:", columns)
    #print("Registros:", type(registros), len(registros))
    return render_template('plantilla/deteccion.html',titulos=columns,registros=registros,)

#-----------reporte PDF-----------

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
 

   

 

    



