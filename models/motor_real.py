import requests
from config import HOST_RASP, PORT_RASP

class Motor:
    def __init__(self):
        self.url_API = f"http://{HOST_RASP}:{PORT_RASP}"

    def adelante(self, vel=50):
        return self.enviar("adelante", vel)

    def atras(self, vel=50):
        return self.enviar("atras", vel)

    def detener(self):
        return self.enviar("detener", 0)

    def obtener_estado(self):
        r = requests.get(f"{self.url_API}/estado")
        return r.json()

    def enviar(self,accion, velocidad):
        #diccionario
        datos_motor = {
            "accion": accion,
            "velocidad": velocidad
        }
        #envio peticion HTTP tipo POST al microservicio 
        respuesta_server = requests.post(f"{self.url_API}/motor", json=datos_motor)
        return respuesta_server.json()