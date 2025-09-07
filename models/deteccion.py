from models.db import getConnection #importo la conexión a la BBDD 

def insertDeteccion  (fecha,color_hex, particulas,claridad,flujo,hora):
    conn = getConnection()
    if conn is None:
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #objeto para ejecutar consultas SQL 
        #variable query realiza la consulta, las 3 comillas son sentencia SQL o se 
        #podria separar con comillas simples por fila
        query= """
             INSERT INTO deteccion (fecha,color_hex, particulas,claridad,flujo,hora )
             VALUES (%s, %s, %s, %s, %s, %s)
             RETURNING id_deteccion;            
                """
        #le envio al cursor la consulta realizada guardada en la variable query y la paso
        #como parámetro
        cursor.execute(query,(fecha,color_hex, particulas,claridad,flujo,hora))
        #retorna el id de la deteccion acabada de agregar, pero podria no retornar nada si quiero
        # quiero controlar o ver que guarda entonces recupero una sola fila del resultado de la consulta
        id_deteccion= cursor.fetchone()[0]
        conn.commit()
        cursor.close() #permite cerrar el cursor que es el que permite scripts SQL 
        conn.close()
        return id_deteccion #puede ser así para que solo devuelva un entero 
        #return f"id insertado: {id_deteccion}"
    except Exception as e:
        return f"Error al insertar: {e}"
    
def getDeteccion():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_deteccion, fecha,color_hex,particulas,claridad,flujo,hora FROM deteccion ORDER BY fecha_hora DESC")
    registros = cursor.fetchall() #devuelve los registros que resultan de consulta ejecutada previamente
    cursor.close()
    conn.close()
    return registros

#modificar consulta...
def getDeteccionId(id_deteccion):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_deteccion, fecha,color_hex,particulas,claridad,flujo,hora FROM deteccion " \
    "WHERE id_deteccion = %s ",(id_deteccion,))
    registro = cursor.fetchone() #devuelve el registro único por el id
    cursor.close()
    conn.close()
    return registro
    