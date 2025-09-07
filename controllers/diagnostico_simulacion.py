from flask import Blueprint, render_template, request
from datetime import datetime
from models.deteccion_diagnostico import insertDetdia
from models.deteccion import getDeteccionId # obtener deteccion por el id de acuerdo a la deteccion en la imagen
from models.diagnostico import getDiagnosticoId
from models.deteccion_diagnostico import insertDetdia


#consulto deteccion y aplico clasificador 

def analisisDeteccion(id_deteccion):
   deteccion= getDeteccionId(id_deteccion)  
   if deteccion[3]:
    ''' 
    si en la deteccion hay particulas entonces
    consulte el diagnostico 1 e igualelo al id diagnostico 
    e inserte el id de la deteccion y el id del diagnostico traido a la tabla det_dia en la BBDD

    si tiene un color ... repita el proceso 11 veces...
    1 LCR NORMAL  PARTICULAS TRUE
2 HEMORRAGIA ANTIGUA COLOR #FFFACD
3 HIPERPROTEINEMIA COLOR #FFD700
4 HEMORRAGIA SUBARANOICDEA FLUJO TRUE 
5 COLOR #8B0000
6.#98FB98 COLOR
7. COLOR #228B22
8
9
10
11 COLOR #FFA500

ahora necesito que de la deteccion que realizo de los parametros los reciba otra funcion para el algoritmo del diagnostico 

si particulas false traiga el diagnostico de id 1. '''



