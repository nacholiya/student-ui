import mysql.connector
from backend.config import Config
from backend.db.exceptions import DatabaseError


def get_db_connection():
    try:
        return mysql.connector.connect(**Config.DB_CONFIG)
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to connect to database") from e
