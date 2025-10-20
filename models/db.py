import psycopg2

def getConnection():
    try:
       conn = psycopg2.connect(
        dbname="robotLCR",
        user="user_robot",
        password="7888",
        host="localhost",
        port="5432"
    )
       return conn
    except Exception as e:
        print ("u_u Error de conexión a la BBDD: ", e)
        return None

    