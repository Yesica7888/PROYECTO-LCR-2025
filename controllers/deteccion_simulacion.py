from flask import render_template, request
from datetime import datetime
from models.deteccion import insertDeteccion
from  controllers.imagen_simulacion import generateImg
