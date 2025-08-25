from flask import Flask  
from controllers.main import main 

#app = Flask(__name__)
#app.register_blueprint(main) #registre este archivo porque alli estan las rutas que voy a usar en la app principal es decir aca

#if __name__ == "__main__":
#    app.run (debug=True, port=5000) 

#probando la plantilla

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(main)

if __name__ == "__main__":
    app.run (debug=True, port=5000) 