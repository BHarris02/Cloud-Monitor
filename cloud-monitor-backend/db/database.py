import mysql.connector # type: ignore
from config import DB_CONFIG

def get_db_connection() -> None:
    return mysql.connector.connect(**DB_CONFIG)