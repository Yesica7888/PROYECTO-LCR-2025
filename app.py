from flask import Flask  #averiguar porque uno mayuscula y el otro minuscula
from controllers.main import main 

app = Flask(__name__)
app.register_blueprint(main) #que hace esta linea

if __name__ == "__main__":
    app.run (debug=True, port=5000) 