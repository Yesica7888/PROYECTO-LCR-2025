from flask import Blueprint, render_template, jsonify
#from models.motor import Motor   [motor simulado]
from models.motor_real import Motor

#nombre del bp con que se va a crear la ruta y "electronica" se llama en la vista 
electronica_bp = Blueprint('electronica',__name__)

#-------------Movimiento simulado-------------------



#--------Movimiento real----------------------

#llamo a la clase motor del modelo 
motor = Motor()

@electronica_bp.route("/movimiento/<accion>", methods=["POST"])
def mov_motores(accion):
 try:
     if accion == "adelante":
        estado = motor.adelante()
     elif accion == "atras":
        estado = motor.atras()
     elif accion == "detener":
        estado = motor.detener()
     else:
        return jsonify({"error": "Acción inválida"}), 400

     return jsonify(estado)
 except Exception as e:
     return jsonify({"error controlador": str(e)}), 500
#--------------------------------------------------

#presion intracraneal
@electronica_bp.route('/PIC')
def presion():
    return render_template('plantilla/presion-intracraneal.html')

#temperatura
@electronica_bp.route('/temperatura')
def temperatura():
    return render_template('plantilla/temperatura.html')

