import mysql.connector
from backend.config import Config


def get_db_connection():
    return mysql.connector.connect(**Config.DB_CONFIG)
