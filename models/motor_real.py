"""
import RPi.GPIO as GPIO

class Motor:

    def __init__(self):
        self.IN1 = 17
        self.IN2 = 18
        self.EN  = 22

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.EN, GPIO.OUT)

        self.pwm = GPIO.PWM(self.EN, 1000)
        self.pwm.start(0)

    def adelante(self, velocidad=60):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(velocidad)

    def atras(self, velocidad=60):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(velocidad)

    def detener(self):
        self.pwm.ChangeDutyCycle(0)
        
"""