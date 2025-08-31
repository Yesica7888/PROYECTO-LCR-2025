from flask import Blueprint, render_template
from models.deteccion import insertDeteccion  # funciones en el archivo deteccion en el modelo del proyecto
from models.diagnostico import insertDiagnostico
from datetime import datetime # para usar la fecha 

main= Blueprint('main', __name__ ,template_folder='templates')

@main.route('/jhon' , endpoint="index")   
def index():
        resultado = 5 #simulando detección 
        return render_template ("plantilla/index.html", resultado=resultado) #de la carpeta templates accede al index


#@main.route('/s')
#def index():
#    resultado = 5 #simulando detección 
#    return render_template ("index.html", resultado=resultado) #de la carpeta templates accede al index

#@main.route('/')
#def index():
#    color_hex= "#FFFF00"
#    particulas = False
#    claridad= ""
#    flujo = "fluido"    

"""
@main.route('/simularDeteccion')
def simularDeteccion():     
    #hora = datetime.now()   
    #fecha = hora.date()     
    #hora = hora.time()  
    fecha=datetime.now().date()
    hora=datetime.now().time()

    color_hex = "#FFFFFF"
    particulas = False
    claridad = True
    flujo = True

    resultado= insertDeteccion (fecha, color_hex,particulas,claridad,flujo,hora)
   #return resultado
    return render_template ("index.html", resultado=resultado)

@main.route('/simularDiagnostico')
def simularDiagnostico():     
    
    diagnostico = "Ictericia"
    descripcion = "presencia de restos celulares o patógenos frecuente en hemorragias"
    
    resultado= insertDiagnostico (diagnostico,descripcion)
   #return resultado
    return render_template ("index.html", resultado=resultado)

    """