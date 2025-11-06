from flask import Flask  
from controllers.main import main 
from controllers.imagen_simulacion import image_bp
from controllers.electronica import electronica_bp  #variable de bp 
#from controllers.reporte import reporte_bp


#app = Flask(__name__)
#app.register_blueprint(main) #registre este archivo porque alli estan las rutas que voy a usar en la app principal es decir aca

#if __name__ == "__main__":
#    app.run (debug=True, port=5000) 

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(electronica_bp) 
#app.register_blueprint(reporte_bp)

if __name__ == "__main__":
  app.run (debug=True, port=5000) 






#probando la plantilla

#app = Flask(__name__, template_folder="templates", static_folder="static")
#app.register_blueprint(main)

#if __name__ == "__main__":
#    app.run (debug=True, port=5000, host='0.0.0.0') 

#FUNCIONAL 

#from flask import Flask, jsonify
#from controllers.imagen_simulacion import image_bp #se importa el bp

#def create_app():
#    app = Flask(__name__)
 # Registrar el blueprint del controlador de imágenes
#    app.register_blueprint(image_bp) #se registra el bp 
#    return app

#if __name__ == "__main__":
#    app = create_app()
#    app.run(debug=True)


#if __name__ == "__main__":
#  app.run(debug=True)

