from models.db import getConnection #importo la conexión a la BBDD del archivo db.py para subir las imagenes a la BBDD

#función para insertar una imagen
#debo enviarle la deteccion a la que lo asocia, es decir que antes de guardar en la BBDD la imagen ya
#debe tener una detección
def insertImagen (ruta_imagen,fk_id_deteccion): 
    conn = getConnection()
    if conn is None:
        return "Error al conectar a la BBDD u_U"
    try:
        cursor= conn.cursor() #objeto para ejecutar consultas SQL 
        #el id es autoincrementable
        query= """
             INSERT INTO imagen (ruta_imagen,fk_id_deteccion)
             VALUES (%s, %s)
             RETURNING id_imagen;            
                """
        #ejecuta la sentencia SQL y envia por parámetro los atributos 
        cursor.execute(query,(ruta_imagen,fk_id_deteccion))
        #retorna el id de la imagen agregada
        # recupero una fila del resultado de la columna
        id_imagen= cursor.fetchone()[0] #fetch es una función,no olvidar los paréntesis
        conn.commit()
        cursor.close() #cerrar el cursor  
        conn.close()
        #return id_imagen puede ser así o:
        return f"id imagen insertada: {id_imagen}"
    except Exception as e:
        return f"Error al insertar: {e}"