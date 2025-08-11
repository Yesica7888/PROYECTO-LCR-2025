import psycopg2

def getConnection():
    return psycopg2.connect(
        dbname="robotLCR",
        user="user_robot",
        password="robotlcr",
        host="localhost",
        port="5432"
    )