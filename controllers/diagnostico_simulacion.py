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
   
    





