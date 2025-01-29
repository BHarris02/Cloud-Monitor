import mysql.connector # type: ignore
from config import DATABASE_URI

def get_db_connection() -> None:
    return mysql.connector.connect(DATABASE_URI)