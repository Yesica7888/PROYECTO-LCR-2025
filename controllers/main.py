from flask import Blueprint, render_template
from models.deteccion import getTotalDeteccion  
from models.deteccion_diagnostico import getDetDiaResumen #O_O


main= Blueprint('main', __name__ )

@main.route('/r')   
def index(): #con este nombre se llama en el index.html
    totalDetecciones= getTotalDeteccion() #total detecciones 
    # Tabla de resumen  
    columns,registros= getDetDiaResumen()
    print("Columns:", columns)
    print("Registros:", type(registros), len(registros))
    
    return render_template ("plantilla/index.html", resultado=totalDetecciones, titulos=columns,registros=registros) #de la carpeta templates accede al index


