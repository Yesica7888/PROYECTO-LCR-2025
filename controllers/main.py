from flask import Blueprint, render_template
from models.deteccion import insertDeteccion  # funciones en el archivo deteccion en el modelo del proyecto
from models.diagnostico import insertDiagnostico
from datetime import datetime # para usar la fecha 

main= Blueprint('main', __name__ ,template_folder='templates')

@main.route('/jhon' , endpoint="index")   
def index():
        resultado = 5 #simulando detección 
        return render_template ("plantilla/index.html", resultado=resultado) #de la carpeta templates accede al index

#rutas temporales para prueba de la plantilla

@main.route("/charts")
def charts(): return render_template("plantilla/charts.html")

@main.route("/tables")
def tables(): return render_template("plantilla/tables.html")

@main.route("/login")
def login(): return render_template("plantilla/login.html")

@main.route("/register")
def register(): return render_template("plantilla/register.html")

@main.route("/password")
def password(): return render_template("plantilla/password.html")

@main.route("/layout-static")
def layout_static(): return render_template("plantilla/layout-static.html")

@main.route("/layout-sidenav-light")
def layout_sidenav_light(): return render_template("plantilla/layout-sidenav-light.html")

@main.route("/401")
def error_401(): return render_template("plantilla/401.html")

@main.route("/404")
def error_404(): return render_template("plantilla/404.html")

@main.route("/500")
def error_500(): return render_template("plantilla/500.html")

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