from models.db import getConnection #importo la conexión a la BBDD del archivo db.py

#función para insertar un diagnostico
def insertDiagnostico  (diagnostico,descripcion):
    conn = getConnection()
    if conn is None:
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #objeto para ejecutar consultas SQL 
        #el id es autoincrementable
        query= """
             INSERT INTO diagnostico (diagnostico,descripcion )
             VALUES (%s, %s)
             RETURNING id_diagnostico;            
                """
        #ejecuta la sentencia SQL y envia por parámetro los atributos 
        cursor.execute(query,(diagnostico,descripcion))
        #retorna el id del diagnostico
        # recupero una fila del resultado de la columna
        id_diagnostico= cursor.fetchone()[0] #fetch es una función,no olvidar los paréntesis
        conn.commit()
        cursor.close() #cerrar el cursor  
        conn.close()
        #return id_diagnostico puede ser así o:
        return f"id diagnostico insertado: {id_diagnostico}"
    except Exception as e:
        return f"Error al insertar: {e}"
    
def getDiagnostico():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_dignostico,diagnostico ,descripcion FROM diagnostico ORDER BY id_diagnostico DESC")
    registros = cursor.fetchall() #devuelve los registros que resultan de consulta ejecutada previamente
    cursor.close()
    conn.close()
    return registros
     