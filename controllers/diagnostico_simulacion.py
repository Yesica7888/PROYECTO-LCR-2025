from models.deteccion_diagnostico import insertDetdia
from models.deteccion import getDeteccionId # obtener deteccion por el id de acuerdo a la deteccion en la imagen
from models.diagnostico import getDiagnosticoId
from models.deteccion_diagnostico import insertDetdia



#declaro los colores fijos que no van a cambiar ids de cada diagnostico

COLORESDIAGNOSTICO = {
 "#FFFFFF":1,  # LCR NORMAL
 "#FFFACD":2,  # HEMORRAGIA ANTIGUA
 "#FFD700":3,  # HIPERPROTEINEMIA
 "#FFC0CB":4, # HEMORRAGIA SUBARACNOIDEA
 "#8B0000":5,  # HEMORRAGIA TRAUMÁTICA
 "#98FB98":6,  # INFECCIÓN BACTERIANA
 "#228B22":7,  # MENINGITIS PURULENTA
 "#E6E68A":8,  # MENINGITIS TUBERCULOSA
 "#F2F2F2":9,  # CRIPTOCOCOSIS
 "#F5F5F5":10, # METÁSTASIS O CÁNCER
 "#FF6666":11  # ABSCESO CEREBRAL
}

# diccionario usado para la vista

NOMBRESCOLORES = {
"#FFFFFF": "Transparente",            # LCR NORMAL
"#FFFACD": "Amarillo muy pálido",      # HEMORRAGIA ANTIGUA
"#FFD700": "Amarillo intenso",         # HIPERPROTEINEMIA
"#FFC0CB": "Rosado",                   # HEMORRAGIA SUBARACNOIDEA
"#8B0000": "Rojo oscuro",              # HEMORRAGIA TRAUMÁTICA
"#98FB98": "Verde pálido",              # INFECCIÓN BACTERIANA
"#228B22": "Verde oscuro",              # MENINGITIS PURULENTA
"#E6E68A": "Amarillo opaco",            # MENINGITIS TUBERCULOSA
"#F2F2F2": "Blanco grisáceo",           # CRIPTOCOCOSIS
"#F5F5F5": "Blanco lechoso",            # METÁSTASIS O CÁNCER
"#FF6666": "Rojo claro"                 # ABSCESO CEREBRAL
}

    
#funcion para analisis de la deteccion realizada 
def analisisDeteccion(id_deteccion):
    #obtengo la deteccion completa tupla  
    deteccion = getDeteccionId(id_deteccion) 
    #capturo el id de la deteccion 
    id_det= deteccion[0]

   # funcion auxiliar para obtener el diagnostico depende las condiciones de la deteccion
    def insercion(id):
      #obtengo tupla con diagnostico completo por id
      diagnostico=getDiagnosticoId(id)
      if diagnostico is None:
        return None, (None, "Diagnóstico no encontrado")
      #extraigo su id
      id_diagnostico= diagnostico[0]
      #recibe la deteccion ,la asocia con un diagnostico y obtengo id del diagnostico
      id_detdia =insertDetdia(id_det,id_diagnostico)
      #retorno el id de la deteccion asociada al diagnostico y el diagnostico completo
      return id_detdia,diagnostico
#condiciones para generar el diagnostico
    if deteccion[2] ==  "#FFFFFF" and not deteccion[3] and deteccion[4] and deteccion[5] :
     return insercion(1)
    elif deteccion[2] == "#FFFACD" and deteccion[3] and not deteccion[4] and not deteccion[5]:
      return insercion(2)
    elif deteccion[2] == "#FFD700" and deteccion[3] and not deteccion[4] and not deteccion[5] :
      return insercion(3)
    elif deteccion[2] == "#FFC0CB" and deteccion[3]and not deteccion[4] and deteccion[5]:
      return insercion(4)
    elif deteccion[2] == "#8B0000" and deteccion[3] and not deteccion[4] and not deteccion[5] :
      return insercion(5)
    elif deteccion[2] == "#98FB98" and deteccion[3] and not deteccion[4] and not deteccion[5] :
      return insercion(6)
    elif deteccion[2] == "#228B22" and deteccion[3] and not deteccion[4] and not deteccion[5]:
      return insercion(7)
    elif deteccion[2] == "#E6E68A" and deteccion[3] and not deteccion[4] and not deteccion[5]:
      return insercion(8)
    elif deteccion[2] == "#F2F2F2" and deteccion[3] and not deteccion[4] and not deteccion[5]:
      return insercion(9)
    elif deteccion[2] == "#F5F5F5" and deteccion[3] and not deteccion[4] and not deteccion[5]:
      return insercion(10)
    elif deteccion[2] == "#FF6666" and deteccion[3] and not deteccion[4] and not deteccion[5]:
      return insercion(11)
    else:
      return None,(None,"No se puede asociar a ningun diagnostico conocido")  #para mantener formato




