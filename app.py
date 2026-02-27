from flask import Flask  
from controllers.main import main 
from controllers.imagen_simulacion import image_bp
from controllers.electronica import electronica_bp  #variable de bp 
#from controllers.reporte import reporte_bp

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(electronica_bp) 
app.register_blueprint(image_bp)

#app.register_blueprint(reporte_bp)

#clave para la sesion, mostrar resultados temporales  
app.secret_key = "dev-010011000100001101010010"

if __name__ == "__main__":
  app.run (debug=True, port=5000) 






