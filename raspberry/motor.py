from flask import Flask, request, jsonify
import time
import RPi.GPIO as GPIO

# Pines 
IN1 = 17    
IN2 = 27
ENA = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

app = Flask(__name__)

estado_motor = {
    "estado": "DETENIDO RASP",
    "velocidad": 0
}

# motor movimiento
def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def motor_backward(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)

# API REST 
@app.route("/motor", methods=["POST"])
def controlar_motor():
    data = request.json
    
    if not data:
     return jsonify ({"ERROR RASP": "JSON inválido o vacio"})
    
    accion = data.get("accion")
    velocidad = data.get("velocidad", 50)

    if accion == "adelante":
        motor_forward(velocidad)
        estado_motor.update({"estado": "ADELANTE RASP", "velocidad": velocidad})

    elif accion == "atras":
        motor_backward(velocidad)
        estado_motor.update({"estado": "ATRAS RASP", "velocidad": velocidad})

    elif accion == "detener":
        motor_stop()
        estado_motor.update({"estado": "DETENIDO RASP", "velocidad": 0})

    return jsonify(estado_motor)

@app.route("/estado", methods=["GET"])
def estado():
    return jsonify(estado_motor)
    
# main
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        motor_stop()
        GPIO.cleanup()