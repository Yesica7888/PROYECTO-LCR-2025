class Bluetooth:
    def __init__(self):
        self.estado = "desconectado"

    def conectar(self):
        if self._estado == "conectado":
            return {
                "estado": self.estado,
                "mensaje": "El Bluetooth ya está conectado"
            }

        self._estado = "conectado"
        return {
            "estado": self.estado,
            "mensaje": "Bluetooth conectado correctamente"
        }

    def desconectar(self):
        if self._estado == "desconectado":
            return {
                "estado": self.estado,
                "mensaje": "El Bluetooth ya estaba desconectado"
            }

        self._estado = "desconectado"
        return {
            "estado": self.estado,
            "mensaje": "Bluetooth desconectado correctamente"
        }

    def obtener_estado(self):
        return self.estado