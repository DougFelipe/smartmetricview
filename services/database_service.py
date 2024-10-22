import psycopg2
from psycopg2 import OperationalError

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="minha_aplicacao",
            user="usuario",
            password="usuario",
            host="localhost",
            port="5432"
        )
        print("Conexão bem-sucedida!")
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
