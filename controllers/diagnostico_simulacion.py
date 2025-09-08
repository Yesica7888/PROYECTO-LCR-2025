from flask import Blueprint, render_template, request
from datetime import datetime
from models.deteccion_diagnostico import insertDetdia
from models.deteccion import getDeteccionId # obtener deteccion por el id de acuerdo a la deteccion en la imagen
from models.diagnostico import getDiagnosticoId
from models.deteccion_diagnostico import insertDetdia


#declaro los colores fijos que no van a cambiar 

COLORESDIAGNOSTICO = {
 "#FFFACD":2,
 "#FFD700":3,
 "#8B0000":5,
 "#98FB98":6,
 "#228B22":7,
 "#E6E68A":8,
 "#F2F2F2":9,
 "#F5F5F5":10,
 "#FF6666":11
}

#consulto deteccion y aplico clasificador 

def analisisDeteccion(id_deteccion):
   deteccion= getDeteccionId(id_deteccion) 
   id_det= deteccion[0] 
  
   def insercion(id):
     diagnostico=getDiagnosticoId(id)
     id_diagnostico=diagnostico[0]
     id_detdia =insertDetdia(id_det,id_diagnostico)
     return id_detdia,diagnostico

#condicion pregunta sobre atributos de la deteccion 
   if not deteccion[3]: # si particulas false
    return insercion(1) #envia el id del diagnostico recibe el id del diagnostico asociado a deteccion
   elif deteccion[5]:# si flujo true
    return insercion(4) #diagnostico 4
   elif deteccion[2] in COLORESDIAGNOSTICO: # unico diferenciador es color 
    return insercion(COLORESDIAGNOSTICO[deteccion[2]])
   else:
    return "no se pudo asociar a ningún diagnóstico conocido"
   
    

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



