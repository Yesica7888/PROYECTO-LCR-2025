from models.db import getConnection #conexión a la BBDD

def insertDetdia(id_deteccion): #recibe la deteccion para asociarla a un diagnostico
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
       #¿cómo manejo el tema de los colores si no en todos es el mismo, debería tener unos rangos?
       #por ahora voy a llamar a todos los parámetros u_U , no es óptimo
       # ¿Al asociar una detección con un diagnostico es importante traer la fecha y hora? NO
       
        query = """
                SELECT (color_hex,particulas,claridad,flujo)
                FROM deteccion
                WHERE id_deteccion = %s
            """

    except Exception as e:
        return f"Error al insertar: {e}"