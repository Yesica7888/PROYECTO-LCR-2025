from flask import Blueprint, render_template
from models.deteccion import getTotalDeteccion  
from models.deteccion_diagnostico import getDetDiaResumen #O_O


main= Blueprint('main', __name__ )

@main.route('/r')   
def index(): #con este nombre se llama en el index.html
    totalDetecciones= getTotalDeteccion() #total detecciones 
    # pendiente mostrar tabla de resumen O_O


    return render_template ("plantilla/index.html", resultado=totalDetecciones) #de la carpeta templates accede al index


