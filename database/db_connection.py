import pymysql
from database.config import db_config  # adjust the path if needed

def get_connection():
    return pymysql.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"],
        port=db_config.get("port", 3306),
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query, params=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
        connection.commit()
    finally:
        connection.close()

def fetch_query(query, params=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result
    finally:
        connection.close()
