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