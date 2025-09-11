from flask import Blueprint, render_template
from models.deteccion import getTotalDeteccion  


main= Blueprint('main', __name__ )

@main.route('/r')   
def index(): #con este nombre se llama en el index.html
    totalDetecciones= getTotalDeteccion()
    return render_template ("plantilla/index.html", resultado=totalDetecciones) #de la carpeta templates accede al index


