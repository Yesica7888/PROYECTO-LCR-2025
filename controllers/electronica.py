from flask import Blueprint, render_template, jsonify
from models.bluetooth import Bluetooth

#nombre del bp con que se va a crear la ruta y "electronica" se llama en la vista 
electronica_bp = Blueprint('electronica',__name__)

#llamo a clase del modelo para la conexión no persiste
bluetooth= Bluetooth()

# blueprint para bluetooth 

@electronica_bp.route('/bluetooth')
def conexion():
    return render_template('plantilla/con-bluetooth.html')

@electronica_bp.route('/bluetooth/conectar', methods=['POST'])
def conectar():
    return jsonify(bluetooth.conectar())

@electronica_bp.route('/bluetooth/desconectar', methods=['POST'])
def desconectar():
    return jsonify(bluetooth.desconectar())

@electronica_bp.route('/bluetooth/estado')
def estado():
    return jsonify({
        "estado": bluetooth.obtener_estado()
    })


#--------------------------------------------

@electronica_bp.route('/movimiento')
def mov_motores():
    return render_template('plantilla/movimiento-bot.html')

#presion intracraneal
@electronica_bp.route('/PIC')
def presion():
    return render_template('plantilla/presion-intracraneal.html')

#temperatura
@electronica_bp.route('/temperatura')
def temperatura():
    return render_template('plantilla/temperatura.html')

