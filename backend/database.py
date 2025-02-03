#Conexão com o banco de dados
import psycopg2
import os

def connect_db():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "postgresql"),
        user=os.getenv("DB_USER", "giovann4m"),
        password=os.getenv("DB_PASSWORD", "admin123"),
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432")
    )
    return conn
