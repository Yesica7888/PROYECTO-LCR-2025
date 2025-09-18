from models.db import getConnection #conexión a la BBDD


def insertDetdia(fk_id_deteccion,fk_id_diagnostico): #recibe la deteccion para asociarla a un diagnostico
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
       
        query = """
                INSERT INTO deteccion_diagnostico (fk_id_deteccion,fk_id_diagnostico)
                VALUES (%s,%s)
                RETURNING id_det_dia;
            """
        #ejecuta la sentencia SQL y envia por parámetro los atributos 
        cursor.execute(query,(fk_id_deteccion,fk_id_diagnostico))
        #retorna el id de la relacion entre deteccion y diagnostico agregada
         # recupero una fila del resultado de la columna
        id_det_dia= cursor.fetchone()[0] #fetch es una función,no olvidar los paréntesis
        conn.commit()
        cursor.close() #cerrar el cursor  
        conn.close()
        return f"id deteccion diagnostico insertado: {id_det_dia}"
    except Exception as e:
        return f"Error al insertar: {e}"
    

def getDetDiaResumen():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
       
        query = """
                SELECT detdia.id_det_dia AS "N° Detección",det.fecha AS "Fecha",
                det.hora AS "Hora",dia.diagnostico AS "Diagnostico",dia.descripcion AS "Desripción",
                i.ruta_imagen AS "Imagen"
                FROM deteccion_diagnostico AS detdia
                INNER JOIN deteccion AS det 
                ON detdia.fk_id_deteccion = det.id_deteccion
                INNER JOIN diagnostico AS dia
                ON detdia.fk_id_diagnostico= dia.id_diagnostico
                INNER JOIN imagen AS i
                ON i.fk_id_deteccion = det.id_deteccion
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        # Alias de las columnas    
        columns= [alias[0] for alias in cursor.description]
        registros= cursor.fetchall() # trae los registros de la consulta
        conn.commit()
        cursor.close() #cerrar el cursor  
        conn.close()
        return columns, registros
    except Exception as e:
        return f"Error al insertar: {e}"
    

   