from flask import Blueprint, render_template

#nombre del bp con que se va a crear la ruta y "electronica" se llama en la vista 
electronica_bp = Blueprint('electronica',__name__)

# pendiente desarrollo prueba para conexion de bluetooth pero despues sera un modulo independiente
@electronica_bp.route('/bluetooth')
def conexion():
    return render_template('plantilla/con-bluetooth.html')

@electronica_bp.route('/movimiento')
def mov_motores():
    return render_template('plantilla/movimiento-bot.html')

@electronica_bp.route('/PIC')
def presion():
    return render_template('plantilla/presion-intracraneal.html')

@electronica_bp.route('/temperatura')
def temperatura():
    return render_template('plantilla/temperatura.html')


