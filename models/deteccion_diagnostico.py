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
        conn.commit() # debe ir el commit si o si porque el un cambio en la BBDD , en operaciones como SELECT no se usa
        cursor.close() #cerrar el cursor  
        conn.close()
        return id_det_dia
    except Exception as e:
        return f"Error al insertar: {e}"
    
#Tabla resumen deteccion asociado a diagnostico

def getDetDiaResumen():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
           
      #tabla que resume los diagnosticos, con las detecciones realizadas 
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
        # Alias de las columnas "AS" en la consulta   
        columns= [alias[0] for alias in cursor.description]
        registros= cursor.fetchall() # trae los registros de la consulta
        cursor.close() #cerrar el cursor  
        conn.close()
        return columns, registros
    except Exception as e:
        return f"Error al consultar: {e}"

#detecciones con riesgo bajo
    
def get_total_riesgo_bajo():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT COUNT(dd.id_det_dia) AS total
                FROM deteccion_diagnostico AS dd
                INNER JOIN diagnostico AS dia
                ON dd.fk_id_diagnostico = dia.id_diagnostico
                WHERE dia.id_diagnostico IN  (1,2)
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        # consulta se retorna como una tupla de  valor, por eso se debe recibir :[0]       
        total_riesgo_bajo= cursor.fetchone()[0]
        cursor.close() #cerrar el cursor  
        conn.close()
        return total_riesgo_bajo
    except Exception as e:
        return f"Error al consultar: {e}"
   
#detecciones con riesgo moderado PENDIENTE 
    
def get_total_riesgo_moderado():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT COUNT(dd.id_det_dia) AS total
                FROM deteccion_diagnostico AS dd
                INNER JOIN diagnostico AS dia
                ON dd.fk_id_diagnostico = dia.id_diagnostico
                WHERE dia.id_diagnostico IN  (10,8,9,3,5)
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        # consulta se retorna como una tupla de  valor, por eso se debe recibir :[0]       
        total_riesgo_moderado= cursor.fetchone()[0]
        cursor.close() #cerrar el cursor  
        conn.close()
        return total_riesgo_moderado
    except Exception as e:
        return f"Error al consultar: {e}"

  
def get_total_riesgo_alto():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT COUNT(dd.id_det_dia) AS total
                FROM deteccion_diagnostico AS dd
                INNER JOIN diagnostico AS dia
                ON dd.fk_id_diagnostico = dia.id_diagnostico
                WHERE dia.id_diagnostico IN  (4,7,6,11)
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        # consulta se retorna como una tupla de  valor, por eso se debe recibir :[0]       
        total_riesgo_alto= cursor.fetchone()[0]
        cursor.close() #cerrar el cursor  
        conn.close()
        return  total_riesgo_alto
    except Exception as e:
        return f"Error al consultar: {e}"
   
def get_total_por_diagnostico():
    conn = getConnection() # conexion a la base de datos 
    if conn is None:
        return "Error al conectar a la BBDD u_U "
    try:
        cursor= conn.cursor() #objeto que permite recorrer secuencialmente los resultados fila por fila de una consulta :)
        
        #consulta para obtener el total de cada diagnostico simulado
        query = """
                SELECT dia.diagnostico AS diagnostico, COUNT (detdia.fk_id_diagnostico) AS total
                FROM diagnostico AS dia
                INNER JOIN deteccion_diagnostico AS detdia
                ON (dia.id_diagnostico= detdia.fk_id_diagnostico)
                GROUP BY dia.diagnostico
                ORDER BY total DESC

                """
        #ejecuta la sentencia
        cursor.execute(query)
        registros= cursor.fetchall() # trae todos registros de la consulta
        return registros
    except Exception as e:
        return f"Error en la consulta funcion total por diagnostico: {e}"
    finally: #en caso que haya excepciones o no se cierra la conexion y el cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
#----Consultas para diagramas de barras en el dashboard-----      

#---total detalles---
def get_condiagnostico():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
            
            SELECT d.diagnostico AS diagnostico , COUNT (dd.id_det_dia) AS total
            FROM deteccion_diagnostico AS dd
            INNER JOIN diagnostico AS d
            ON dd.fk_id_diagnostico= d.id_diagnostico
            GROUP BY d.diagnostico
            ORDER BY total DESC
                
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        registros= cursor.fetchall() # trae todos registros de la consulta
        return registros
    except Exception as e:
        return f"Error en la consulta funcion total por diagnostico: {e}"
    finally: #en caso que haya excepciones o no se cierra la conexion y el cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()          
            
#---riesgo bajo detalles---            
def get_diagnosticos_riesgo_bajo():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT d.diagnostico AS diagnostico,COUNT (dd.id_det_dia) AS total
                FROM deteccion_diagnostico AS dd
                INNER JOIN diagnostico AS d
                ON dd.fk_id_diagnostico=d.id_diagnostico
                WHERE d.id_diagnostico IN (1,2)
                GROUP BY d.diagnostico
                ORDER BY total DESC

            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        registros= cursor.fetchall() # trae todos registros de la consulta
        return registros
    except Exception as e:
        return f"Error en la consulta funcion total por diagnostico: {e}"
    finally: #en caso que haya excepciones o no se cierra la conexion y el cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
#---riesgo moderado detalles---              
def get_diagnosticos_riesgo_moderado():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT d.diagnostico AS diagnostico,COUNT (dd.id_det_dia) AS total
                FROM deteccion_diagnostico AS dd
                INNER JOIN diagnostico AS d
                ON dd.fk_id_diagnostico=d.id_diagnostico
                WHERE d.id_diagnostico IN (10,8,9,3,5)
                GROUP BY d.diagnostico
                ORDER BY total DESC
                
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        registros= cursor.fetchall() # trae todos registros de la consulta
        return registros
    except Exception as e:
        return f"Error en la consulta funcion total por diagnostico: {e}"
    finally: #en caso que haya excepciones o no se cierra la conexion y el cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()  
            
#---riesgo alto detalles---              
def get_diagnosticos_riesgo_alto():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT d.diagnostico AS diagnostico,COUNT (dd.id_det_dia) AS total
                FROM deteccion_diagnostico AS dd
                INNER JOIN diagnostico AS d
                ON dd.fk_id_diagnostico=d.id_diagnostico
                WHERE d.id_diagnostico IN (4,7,6,11)
                GROUP BY d.diagnostico
                ORDER BY total DESC
                
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        registros= cursor.fetchall() # trae todos registros de la consulta
        return registros
    except Exception as e:
        return f"Error en la consulta funcion total por diagnostico: {e}"
    finally: #en caso que haya excepciones o no se cierra la conexion y el cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()      
            
#---sin diagnostico detalles---              
def get_sin_diagnostico():
    conn = getConnection() # variable que llama a la función que tiene las credenciales para acceder a la BBDD
    if conn is None: # control de posibles errores
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #obj para ejecutar consultas SQL 
       #En esta consulta traigo los parámetros de la deteccion para asociar a un diagnostico
      
        query = """
                SELECT 'sin_diagnostico' AS estado, COUNT (d.id_deteccion) AS total
                FROM deteccion AS d
                LEFT JOIN deteccion_diagnostico AS dd
                ON d.id_deteccion= dd.fk_id_deteccion 
                WHERE dd.id_det_dia IS NULL 
                
                UNION ALL
                
                SELECT 'con_diagnostico' AS estado, COUNT (d.id_deteccion) AS total
                FROM deteccion AS d
                INNER JOIN deteccion_diagnostico AS dd
                ON  d.id_deteccion = dd.fk_id_deteccion
                
            """
        #ejecuta la sentencia SQL  
        cursor.execute(query)
        registros= cursor.fetchall() # trae todos registros de la consulta
        return registros
    except Exception as e:
        return f"Error en la consulta funcion total por diagnostico: {e}"
    finally: #en caso que haya excepciones o no se cierra la conexion y el cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()     
            
                               
               

    
 